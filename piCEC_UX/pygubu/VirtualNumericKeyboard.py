#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar


class VirtualNumericKeyboard(tk.Toplevel):
    def __init__(self, master=None, fieldStrVar=None, maxDigits=None, **kw):
        self.master = master
        self.fieldStrVar = fieldStrVar
        self.maxDigits = maxDigits

        self.originalValue=self.fieldStrVar.get()

        super().__init__(master, **kw)

        self.protocol("WM_DELETE_WINDOW", self.enter)

        self.messageTooLong = "Too Many Digits, Max = " + str(self.maxDigits)
        self.messageEmpty = ""

        self.message = StringVar()
        self.message.set(self.messageEmpty)

        self.currentPos = len(self.fieldStrVar.get())

        self.grab_set()  # This line makes the cw settings window modal
        self.transient(self.master)  # Makes the cw settings appear above the mainwindow
        toplevel_offsetx, toplevel_offsety = self.master.winfo_x() , self.master.winfo_y()
        padx = 350  # the padding you need.
        pady = 0
        self.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        self.mainframe = ttk.Frame(self)

        rows = [["7", "8", "9"],
                ["4", "5", "6"],
                ["1", "2", "3"],
                ["0", "<", "Del"]]

        for r, row in enumerate(rows, 1):
            for c, t in enumerate(row):
                ttk.Button(self.mainframe, style='Button2Raised.TButton',text="\n"+t+"\n", width=6, command=lambda t=t: self.press(t)).grid(row=r, column=c,pady=1,padx="0 1")

        ttk.Button(self.mainframe, style='Button2Raised.TButton',text="\nClear\n", width=9, command=self.clear).grid(row=len(rows)+1,column=0, columnspan=2,sticky='w',pady=1,padx="0 1")
        ttk.Button(self.mainframe, style='Button2Raised.TButton', text="\nEnter\n", width=9, command=self.enter).grid(row=len(rows)+1, column=1,columnspan=2,sticky='e',pady=1,padx=1)
        ttk.Entry(self.mainframe, style='Entry1b.TEntry', font=('Arial', 18, 'bold'),textvariable=self.message, state="readonly", width=18,justify="center").grid(row=len(rows)+2,column=0,columnspan=3,pady=2,padx="0 1",sticky='ew')

        master.bind("<Return>", self.enter)

        self.mainframe.configure(style='Normal.TFrame', height=200, width=200)
        self.mainframe.pack(fill="both", expand=True, padx=5, pady=5)
        self.configure(background="gray", height=200, width=200)

    def clear(self,event=None):
        cursor = ' '
        self.fieldStrVar.set("")
        self.currentPos = 0
        self.message.set(self.messageEmpty)

    def enter(self,event=None):
        cursor = ' '
        self.fieldStrVar.set(self.fieldStrVar.get().replace(cursor,''))
        if self.originalValue !=self.fieldStrVar.get():
            self.master.Channel_Freq_Changed_CB()
        self.destroy()

    def press(self,t):
        cursor = ' '
        if t == "Del":
            self.currentPos -=  1
            if self.currentPos < self.maxDigits:
                self.message.set(self.messageEmpty)
            first_half = (self.fieldStrVar.get()[:self.currentPos].replace(cursor,''))
            second_half = self.fieldStrVar.get()[self.currentPos+1:].replace(cursor,'')
            self.fieldStrVar.set(first_half  + cursor + second_half)
        elif t == "<":
            self.currentPos -= 1
            if self.currentPos < 0:
                self.currentPos = len(self.fieldStrVar.get())-1
                self.fieldStrVar.set(self.fieldStrVar.get().replace(cursor,'')+cursor)
            else:
                first_half = self.fieldStrVar.get()[:self.currentPos].replace(cursor,'')
                second_half = self.fieldStrVar.get()[self.currentPos:].replace(cursor,'')
                self.fieldStrVar.set(first_half + cursor + second_half)
        else:
            if self.currentPos < self.maxDigits:
                first_half = self.fieldStrVar.get()[:self.currentPos].replace(cursor,'')
                second_half = self.fieldStrVar.get()[self.currentPos:].replace(cursor,'')
                self.fieldStrVar.set(first_half + t + cursor + second_half)
                self.currentPos += 1
            else:
                self.message.set(self.messageTooLong)

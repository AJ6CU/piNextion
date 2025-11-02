#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox


class VirtualKeyboard(tk.Toplevel):
    def __init__(self, master=None, fieldStrVar=None, maxChars=None, **kw):
        self.master = master
        self.fieldStrVar = fieldStrVar
        self.localStrVar = StringVar()
        self.localStrVar.set(self.fieldStrVar.get())

        self.maxChars = maxChars

        self.originalValue=self.fieldStrVar.get()
        self.fieldStrVar.set(self.originalValue.replace(" ",""))
        self.currentPos = len(self.fieldStrVar.get())
        self.maxChars = maxChars
        self.cursor = ' '



        super().__init__(self.master, **kw)



        self.messageTooLong = "Too Many Chars, Max = " + str(self.maxChars)

        self.currentPos = len(self.fieldStrVar.get())

        # self.protocol("WM_DELETE_WINDOW", self.enter)
        self.grab_set()  # This line makes the cw settings window modal
        # self.transient(self.master)  # Makes the appear above the mainwindow

        toplevel_offsetx, toplevel_offsety = self.master.winfo_x() , self.master.winfo_y()
        padx = 0  # the padding you need.
        pady = 0
        self.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")


        self.row1keys = ["`", "1", "2", "3", "4", "5", "6", "7","8", "9", "0", "-", "=", "backspace"]
        self.row2keys = ["q", "w", "e", "r", "t", "y", 'u', 'i', 'o', 'p', '[', ']', 'enter']
        self.row3keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '\\', 'home', 'end']
        self.row4keys = ["left shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm',',', '.', '/', 'right shift']
        self.row5keys = ['spacebar','left', 'right']

        # buttons for each row
        self.row1buttons = []
        self.row2buttons = []
        self.row3buttons = []
        self.row4buttons = []
        self.row5buttons = []

        appendrow1 = self.row1buttons.append
        appendrow2 = self.row2buttons.append
        appendrow3 = self.row3buttons.append
        appendrow4 = self.row4buttons.append
        appendrow5 = self.row5buttons.append

        # prevents frames having inconsistent relative dimensions
        self.master.columnconfigure(0, weight=1)
        for i in range(5):
            self.master.rowconfigure(i, weight=1)

        # create a frame for row1buttons
        keyframe1 = ttk.Frame(self, height=1)
        keyframe1.rowconfigure(0, weight=1)

        # create row1buttons
        for key in self.row1keys:
            ind = self.row1keys.index(key)
            if ind == 13:
                keyframe1.columnconfigure(ind, weight=2)
            else:
                keyframe1.columnconfigure(ind, weight=1)
            appendrow1(ttk.Button(keyframe1,style='Button2Raised.TButton', width=3))
            if key == "backspace":
                self.row1buttons[ind].config(text=key.title(), width=8)

            self.row1buttons[ind].grid(row=0, column=ind, sticky="NSEW", ipadx=8, ipady=8)

        self.row1buttons[0].config(text="~\n`")
        self.row1buttons[1].config(text="!\n1")
        self.row1buttons[2].config(text="@\n2")
        self.row1buttons[3].config(text="#\n3")
        self.row1buttons[4].config(text="$\n4")
        self.row1buttons[5].config(text="%\n5")
        self.row1buttons[6].config(text="^\n6")
        self.row1buttons[7].config(text="&\n7")
        self.row1buttons[8].config(text="*\n8")
        self.row1buttons[9].config(text="(\n9")
        self.row1buttons[10].config(text=")\n0")
        self.row1buttons[11].config(text="_\n-")
        self.row1buttons[12].config(text="+\n=")

        # Row 2

        # create a frame for row2buttons
        keyframe2 = ttk.Frame(self, width=1)
        keyframe2.rowconfigure(0, weight=1)

        # create row2buttons
        for key in self.row2keys:
            ind = self.row2keys.index(key)
            if ind == 13:
                keyframe2.columnconfigure(ind, weight=2)
            else:
                keyframe2.columnconfigure(ind, weight=1)
            appendrow2(ttk.Button(keyframe2,style='Button2Raised.TButton', width=3))
            if key ==  "[":
                self.row2buttons[ind].config(text="{\n[")
            elif key == "]":
                self.row2buttons[ind].config(text="}\n]")
            elif key == "enter":
                self.row2buttons[ind].config(text="Enter")
            else:
                self.row2buttons[ind].config(text=key.title())

            self.row2buttons[ind].grid(row=0, column=ind, sticky="NSEW", ipadx=8, ipady=8)

        #   Row 3

        # create a frame for row3buttons
        keyframe3 = ttk.Frame(self, height=1)
        keyframe3.rowconfigure(0, weight=1)

        # create row4buttons
        for key in self.row3keys:
            ind = self.row3keys.index(key)
            keyframe3.columnconfigure(ind, weight=1)
            appendrow3(ttk.Button(keyframe3,style='Button2Raised.TButton', width=3))
            if key == ";":
                self.row3buttons[ind].config(text=":\n;")
            elif key == "'":
                self.row3buttons[ind].config(text='"\n\'')
            elif key == "\\":
                self.row3buttons[ind].config(text="|\n\\")
            else:
                self.row3buttons[ind].config(text=key.title())

            self.row3buttons[ind].grid(row=0, column=ind, sticky="NSEW", ipadx=8, ipady=8)


    # Row 4
        # create a frame for row4buttons
        keyframe4 = ttk.Frame(self, height=1)
        keyframe4.rowconfigure(0, weight=1)

        # create row4buttons
        for key in self.row4keys:
            ind = self.row4keys.index(key)
            if ind == 0 or ind == 11:
                keyframe4.columnconfigure(ind, weight=3)
            else:
                keyframe4.columnconfigure(ind, weight=1)
            appendrow4(ttk.Button(keyframe4,style='Button2Raised.TButton', width=3))

            if key == ",":
                self.row4buttons[ind].config(text="<\n,")
            elif key == ".":
                self.row4buttons[ind].config(text=">\n.")
            elif key == "/":
                self.row4buttons[ind].config(text="?\n/")
            elif key == "up":
                self.row4buttons[ind].config(text="↑")
            elif key == "left shift":
                self.row4buttons[ind].config(text="Shift", width=6)
            elif key == "right shift":
                self.row4buttons[ind].config(text="Shift", width=6)
            else:
                self.row4buttons[ind].config(text=key.title())

            self.row4buttons[ind].grid(row=0, column=ind, sticky="NSEW", ipadx=8, ipady=8)

    #   ROW 5  #

        # create a frame for row5buttons
        keyframe5 = ttk.Frame(self, height=1)
        keyframe5.rowconfigure(0, weight=1)

        # create row5buttons
        self.entryField = ttk.Entry(keyframe5, style='Entry2Raised.TEntry',textvariable=self.localStrVar)
        keyframe5.columnconfigure(0, weight=0)


        for key in self.row5keys:
            ind = self.row5keys.index(key)
            appendrow5(ttk.Button(keyframe5, style='Button2Raised.TButton', width=3))
            if key == "spacebar":
                print("space found, ind=", ind)
                keyframe5.columnconfigure(ind+1, weight=12)
                self.row5buttons[ind].config(text="Space", width=24)
            elif key == "left":
                self.row5buttons[ind].config(text="<--", width=3)
                keyframe5.columnconfigure(ind + 1, weight=1)
            elif key == "right":
                self.row5buttons[ind].config(text="-->", width=3)
                keyframe5.columnconfigure(ind + 1, weight=1)
            else:
                self.row5buttons[ind].config(text=key.title(), width=3)

        #
        #
        #     if key == "spacebar":
        #         self.row5buttons[ind].config(text="Space", width=10)
        #     else:
        #         self.row5buttons[ind].config(text=key.title())

            # self.row5buttons[ind].grid(row=0, column=ind, sticky="NSEW", ipadx=8, ipady=8)


        self.entryField.grid(row=0, column=0, sticky="NSEW", ipadx=8, ipady=8)
        for key in self.row5keys:
            ind = self.row5keys.index(key)
            print("row5 index =", ind)
            self.row5buttons[ind].grid(row=0, column=ind+1, sticky="NSEW", ipadx=8, ipady=8)



        # add the frames to the main window
        keyframe1.grid(row=1, sticky="NSEW", padx=9, pady=6)
        keyframe2.grid(row=2, sticky="NSEW", padx=9)
        keyframe3.grid(row=3, sticky="NSEW", padx=9)
        keyframe4.grid(row=4, sticky="NSEW", padx=9)
        keyframe5.grid(row=5, sticky="NSEW", padx=9)

        for key in self.row1keys:
            ind = self.row1keys.index(key)
            if key == "backspace":
                self.row1buttons[ind].config(command=self.backspace)
            else:
                self.row1buttons[ind].config(command=lambda x=key: self.vpresskey(x))

        for key in self.row2keys:
            ind = self.row2keys.index(key)
            if key == "enter":
                self.row2buttons[ind].config(command=self.enter)
            else:
                self.row2buttons[ind].config(command=lambda x=key: self.vpresskey(x))


        for key in self.row3keys:
            ind = self.row3keys.index(key)
            if key == "home":
                self.row3buttons[ind].config(command=self.home)
            elif key == "end":
                self.row3buttons[ind].config(command=self.end)
            else:
                self.row3buttons[ind].config(command=lambda x=key: self.vpresskey(x))

        for key in self.row4keys:
            ind = self.row4keys.index(key)
            self.row4buttons[ind].config(command=lambda x=key: self.vpresskey(x))

        for key in self.row5keys:
            ind = self.row5keys.index(key)
            if key == "spacebar":
                self.row5buttons[ind].config(command=lambda x=key: self.vpresskey(" "))
            elif key == "left":
                self.row5buttons[ind].config(command=self.moveLeft)
            elif key == "right":
                self.row5buttons[ind].config(command=self.moveRight)
            else:
                self.row5buttons[ind].config(command=lambda x=key: self.vpresskey(x))




        # for r, row in enumerate(rows, 1):
        #     for c, t in enumerate(row):
        #         ttk.Button(self.mainframe, style='Button2Raised.TButton',text="\n"+t+"\n", width=6, command=lambda t=t: self.press(t)).grid(row=r, column=c,pady=1,padx="0 1")
        #
        # ttk.Button(self.mainframe, style='Button2Raised.TButton',text="\nClear\n", width=9, command=self.clear).grid(row=len(rows)+1,column=0, columnspan=2,sticky='w',pady=1,padx="0 1")
        # ttk.Button(self.mainframe, style='Button2Raised.TButton', text="\nEnter\n", width=9, command=self.enter).grid(row=len(rows)+1, column=1,columnspan=2,sticky='e',pady=1,padx=1)
        # ttk.Entry(self.mainframe, style='Entry1b.TEntry', font=('Arial', 18, 'bold'),textvariable=self.message, state="readonly", width=18,justify="center").grid(row=len(rows)+2,column=0,columnspan=3,pady=2,padx="0 1",sticky='ew')
        #
        # master.bind("<Return>", self.enter)
        #
        # self.mainframe.configure(style='Normal.TFrame', height=200, width=200)
        # self.mainframe.pack(fill="both", expand=True, padx=5, pady=5)
        # self.configure(background="gray", height=200, width=200)

    # def clear(self,event=None):
    #     cursor = ' '
    #     self.fieldStrVar.set("")
    #     self.currentPos = 0
    #     self.message.set(self.messageEmpty)
    #
    def backspace(self):
        if self.currentPos != 0:
            first_half = self.localStrVar.get()[:self.currentPos-1].replace(self.cursor, '')
            second_half = self.localStrVar.get()[self.currentPos + 1:].replace(self.cursor, '')
            self.localStrVar.set(first_half + self.cursor + second_half)
            self.currentPos -= 1

    def enter(self,event=None):
        label = self.localStrVar.get().replace(self.cursor, '')
        self.fieldStrVar.set(label.ljust(5))
        if self.originalValue !=self.fieldStrVar.get():
            self.master.Channel_Freq_Changed_CB()
        self.destroy()

    def home(self):
        print("home called")
        label = self.localStrVar.get().replace(self.cursor, "")
        self.localStrVar.set(self.cursor + label)
        self.currentPos = 0

    def end(self):
        print("end called")
        label = self.localStrVar.get().replace(self.cursor, "")
        self.localStrVar.set(label+self.cursor)
        self.currentPos = len(self.localStrVar.get())-1

    def moveLeft(self):
        print("move left called")
        if self.currentPos == 0:
            return
        self.currentPos -= 1
        first_half = self.localStrVar.get()[:self.currentPos].replace(self.cursor, '')
        second_half = self.localStrVar.get()[self.currentPos:].replace(self.cursor, '')
        self.localStrVar.set(first_half + self.cursor + second_half)

    def moveRight(self):
        print("move right called")
        print(self.currentPos)
        if self.currentPos == self.maxChars-1:
            return
        self.currentPos += 1
        label = self.localStrVar.get().replace(self.cursor, "")
        self.localStrVar.set(label)
        first_half = self.localStrVar.get()[:self.currentPos].replace(self.cursor, '')
        print("*",first_half, "*",sep="+")
        second_half = self.localStrVar.get()[self.currentPos:].replace(self.cursor, '')
        print(second_half)
        self.localStrVar.set(first_half + self.cursor + second_half)






    def vpresskey(self,t):
        if len(self.localStrVar.get().replace(self.cursor,"")) < self.maxChars:
            first_half = self.localStrVar.get()[:self.currentPos].replace(self.cursor,'')
            second_half = self.localStrVar.get()[self.currentPos+1:].replace(self.cursor,'')
            self.localStrVar.set(first_half + t + self.cursor + second_half)
            self.currentPos += 1
        else:
            warning = messagebox.showinfo("Warning", self.messageTooLong, parent=self)

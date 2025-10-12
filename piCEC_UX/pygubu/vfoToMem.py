#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import vfoToMemui as baseui


#
# Manual user code
#

class vfoToMem(baseui.vfoToMemUI):
    def __init__(self, master=None,  mainWindow=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow

    def apply_CB(self):
        print("VFO TO Mem apply CB")
        self.destroy()

    def cancel_CB(self):
        print("VFO To Mem cancel CB")
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = vfoToMem(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

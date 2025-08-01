#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import testMeui as baseui


#
# Manual user code
#

class testMe1(baseui.testMe1UI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


if __name__ == "__main__":
    root = tk.Tk()
    widget = testMe1(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

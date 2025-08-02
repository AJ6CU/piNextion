#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import testbuttonui as baseui
import mystyles


#
# Manual user code
#

class testButtonClass(baseui.testButtonClassUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


if __name__ == "__main__":
    root = tk.Tk()

    widget = testButtonClass(root)
    mystyles.setup_ttk_styles(widget)
    widget.pack(expand=True, fill="both")
    root.mainloop()

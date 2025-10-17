#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelFrame10Plusui as baseui


#
# Manual user code
#

class channelFrame10Plus(baseui.channelFrame10PlusUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelFrame10Plus(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

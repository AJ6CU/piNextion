#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelWrite10PlusFrameui as baseui


#
# Manual user code
#

class channelWrite10PlusFrame(baseui.channelWrite10PlusFrameUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelWrite10PlusFrame(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

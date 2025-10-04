#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import cwSettingsui as baseui


#
# Manual user code
#

class cwSettings(baseui.cwSettingsUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


if __name__ == "__main__":
    root = tk.Tk()
    widget = cwSettings(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

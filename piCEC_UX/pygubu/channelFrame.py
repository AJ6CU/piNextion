#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelFrameui as baseui


#
# Manual user code
#

class channelFrame(baseui.channelFrameUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

    def mem_go_button(self, widget_id):
        print("go button called")
        print("widget id:", widget_id)
        print("parent", self.master.winfo_children())


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelFrame(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

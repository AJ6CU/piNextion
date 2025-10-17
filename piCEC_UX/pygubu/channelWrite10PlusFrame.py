#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelWrite10PlusFrameui as baseui


#
# Manual user code
#


class channelWrite10PlusFrame(baseui.channelWrite10PlusFrameUI):
    changeChannelCallback = None
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)


    def mem_go_button(self):
        print("go button called")
        # print("instance count =", self.channelInstance)
        # channelFrame.changeChannelCallback(self.channelInstance)
        channelFrame.changeChannelCallback(self.Label_VAR.get(),
                                            self.Freq_VAR.get(),
                                            self.Mode_VAR.get(),
                                            self.showLabel_VAR.get())

    def setParentCallback(self, callback):
       channelFrame.changeChannelCallback = callback


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelWrite10PlusFrame(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

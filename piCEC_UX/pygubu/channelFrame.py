#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelFrameui as baseui


#
# Manual user code
#

class channelFrame(baseui.channelFrameUI):
    channelCount = 0
    # changeChannelCallback = None
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        # self.channelInstance = channelFrame.channelCount
        self.showLabel_VAR = tk.StringVar(value='0')
        if channelFrame.channelCount == 9:
            self.Label_VAR.set("Channel 10")
        channelFrame.channelCount += 1
        if channelFrame.channelCount == 10:
            channelFrame.channelCount = 0

    def mem_go_button(self):
        print("go button called")
        # print("instance count =", self.channelInstance)
        # channelFrame.changeChannelCallback(self.channelInstance)
        channelFrame.changeChannelCallback(self.Label_VAR.get(),
                                            self.Freq_VAR.get(),
                                            self.Mode_VAR.get(),
                                            self.showLabel_VAR.get())

    # def setParentCallback(self, callback):
    #    channelFrame.changeChannelCallback = callback


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelFrame(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

import channelFrame10Plusui
import channelFrame10Plusui as baseui


#
# Manual user code
#

class channelFrame10Plus(baseui.channelFrame10PlusUI):
    channelCount = 10
    # changeChannelCallback = None
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.showLabel_VAR = tk.StringVar(value='0')
        self.Label_VAR.set("Channel " + str(channelFrame10Plus.channelCount))
        channelFrame10Plus.channelCount += 1
        if channelFrame10Plus.channelCount == 21:
            channelFrame10Plus.channelCount = 10


    def mem_go_button(self):
        print("go9Plus button called")
        # print("instance count =", self.channelInstance)
        # channelFrame.changeChannelCallback(self.channelInstance)
        channelFrame10Plus.changeChannelCallback(self.Label_VAR.get(),
                                            self.Freq_VAR.get(),
                                            self.Mode_VAR.get(),
                                            self.showLabel_VAR.get())


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelFrame10Plus(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelsui as baseui


#
# Manual user code
#

class channels(baseui.channelsUI):
    channelList = []

    def __init__(self, mainWindow=None, channelCallback=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow
        self.channelCount = 0

        for child in self.scrolledChannelFrame.innerframe.winfo_children():
            channels.channelList.append(child)
            child.assignChannelSelect_CB(channelCallback)
            child.assignChannelNum(self.channelCount)
            self.channelCount += 1



if __name__ == "__main__":
    root = tk.Tk()
    widget = channels(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelsui as baseui


#
# Manual user code
#

class channels(baseui.channelsUI):
    channelList = []

    def __init__(self, master=None, mainWindow=None, channelCallback=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow
        self.channelCount = 0

        for child in self.scrolledChannelFrame.innerframe.winfo_children():
            channels.channelList.append(child)
            child.assignChannelSelect_CB(channelCallback)
            child.assignChannelNum(self.channelCount)
            #
            # Set defaults
            #
            child.channel_Label_Default()
            child.channel_Freq_Default()
            child.select_Channel_Mode_Default()
            child.select_Channel_Showlabel_Default()
            child.select_ScanSet_Default()
            self.scan_Select_Channel_Default()


            self.channelCount += 1

    def scan_Select_Channel_Default(self):
        self.scan_Select_Channel_VAR.set("None")




if __name__ == "__main__":
    root = tk.Tk()
    widget = channels(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

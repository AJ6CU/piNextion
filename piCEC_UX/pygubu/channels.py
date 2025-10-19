#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelsui as baseui


#
# Manual user code
#

class channels(baseui.channelsUI):
    channelList = []
    currentChannel = 0

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
            child.channel_Number_Default()
            child.Label_Default()
            child.Freq_Default()
            child.Mode_Default()
            child.Showlabel_Default()
            child.ScanSet_Default()
            self.scan_Select_Channel_Default()


            self.channelCount += 1

    def scan_Select_Channel_Default(self):
        self.scan_Select_Channel_VAR.set("None")

    def setChanneFreqMode(self, freq, mode):
        channels.channelList[channels.currentChannel].Set_Freq(str(freq))
        channels.channelList[channels.currentChannel].Set_Mode(self.mainWindow.modeNum_To_TextDict[str(mode)])
        channels.currentChannel += 1
        if channels.currentChannel == len(self.channelList):
            channels.currentChannel = 0

    def setChannelLabel(self, label):
        if channels.currentChannel < 10:
            channels.channelList[channels.currentChannel].Set_Label(label)
            channels.currentChannel += 1
        if channels.currentChannel == 10:
            channels.currentChannel = 0

    def setChannelShowLabel(self, showFlag):
        channels.channelList[channels.currentChannel].Set_ShowLabel(showFlag)
        channels.currentChannel += 1
        if channels.currentChannel == 10:
            channels.currentChannel = 0




if __name__ == "__main__":
    root = tk.Tk()
    widget = channels(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

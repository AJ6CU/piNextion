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

    def update_Current_Frequency(self, freq):
        self.current_VFO_VAR.set(freq)

    def update_Current_Mode(self, mode):
        self.current_Mode_VAR.set(mode)


    def scan_Select_Channel_Default(self):
        self.scan_Select_Channel_VAR.set("None")

    def EEPROM_SetChanneFreqMode(self, channelNum,freq, mode):
        channels.channelList[channelNum].Set_Freq(str(freq))
        channels.channelList[channelNum].Set_Mode(self.mainWindow.modeNum_To_TextDict[str(mode)])

    def EEPROM_SetChannelLabel(self, channelNum, label):
        channels.channelList[channelNum].Set_Label(label)

    def EEPROM_SetChannelShowLabel(self, channelNum, showFlag):
        channels.channelList[channelNum].Set_ShowLabel(showFlag)

    def QSY_Channel_CB(self):
        pass




if __name__ == "__main__":
    root = tk.Tk()
    widget = channels(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

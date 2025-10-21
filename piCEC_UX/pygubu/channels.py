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

    def __init__(self, master=None, mainWindow=None, refreshCallback=None,  **kw):

        channels.channelList = []
        channels.currentChannel = 0
        super().__init__(master, **kw)
        self.mainWindow = mainWindow
        self.protocol("WM_DELETE_WINDOW", self.close_Channel_CB)
        self.channelSlotCount = 0
        self.channelSlotSelection = None
        self.savePreset =  int(self.mainWindow.tuning_Preset_Selection_VAR.get())
        self.refreshCallback = refreshCallback


        for child in self.scrolledChannelFrame.innerframe.winfo_children():
            channels.channelList.append(child)
            child.assignChannelSelect_CB(self.channelSlot_CB)
            child.assignChannelNum(self.channelSlotCount)
            #
            # Set defaults
            #
            child.channel_Number_Default()
            child.Label_Default()
            child.Freq_Default()
            child.Mode_Default()
            child.Showlabel_Default()
            child.ScanSet_Default()

            self.channelSlotCount += 1
        self.scan_Select_Channel_Default()

    def update_Current_Frequency(self, freq):
        self.current_VFO_VAR.set(freq)

    def update_Current_Mode(self, mode):
        self.current_Mode_VAR.set(mode)


    def scan_Select_Channel_Default(self):
        self.scan_Select_Channel_VAR.set("None")

    def EEPROM_SetChanneFreqMode(self, channelNum,freq, mode):
        channels.channelList[channelNum].Set_Freq(str(freq))

        # print("EEPROM_SetChanneFreqMode", channels.channelList[channelNum].Get_Freq())
        # print("channel mode type=", type(mode), "mode=", mode)
        # temp = self.mainWindow.modeNum_To_TextDict[str(mode)]
        # print("temp=", temp, type(temp))

        channels.channelList[channelNum].Set_Mode(self.mainWindow.modeNum_To_TextDict[str(mode)])
        # print("finished setChannelFreqMode")


    def EEPROM_SetChannelLabel(self, channelNum, label):
        channels.channelList[channelNum].Set_Label(label)

    def EEPROM_SetChannelShowLabel(self, channelNum, showFlag):
        channels.channelList[channelNum].Set_ShowLabel(showFlag)

    def QSY_Channel_CB(self):               # method called when Channel->VFO
        print("qsy_CB called")
        #
        #   Save tuning preset to restore on close
        #
        # self.savePreset =  int(self.mainWindow.tuning_Preset_Selection_VAR.get())
        self.mainWindow.Radio_Set_Tuning_Preset(1)
        self.mainWindow.Radio_Set_New_Frequency(channels.channelList[self.channelSlotSelection].Get_Freq())
        self.mainWindow.Radio_Set_Mode(self.mainWindow.Text_To_ModeNum[channels.channelList[self.channelSlotSelection].Get_Mode()])
        self.current_Channel_VAR.set(channels.channelList[self.channelSlotSelection].Get_Label())
    def save_Channel_CB(self):              # method called to write current VFO to channel
        print("saveChannel_CB called")

    def scan_Channel_CB(self):              # method called to start channel scanning
        print("scanChannel_CB called")

    def refresh_Channel_CB(self):           # method called when user wants to refresh channels from EEPROM
        print("refresh_CB called within channels")
        self.refreshCallback()

    def close_Channel_CB(self):             # method called when window closed
        print("close_CB called")
        self.mainWindow.Radio_Set_Tuning_Preset(self.savePreset)
        self.withdraw()

    def channelSlot_CB(self, slotNumber):
        print("channel_CB called, channel=", slotNumber+1, "channel slot =", slotNumber)
        if self.channelSlotSelection != None:
            channels.channelList[self.channelSlotSelection].channel_Select_Button.configure(
                style="Button2b.TButton")
            channels.channelList[self.channelSlotSelection].channel_Select_VAR.set("Select")  # unselect the prior one
        self.channelSlotSelection = slotNumber
        channels.channelList[self.channelSlotSelection].channel_Select_Button.configure(
                style="Button2bipressed.TButton")
        channels.channelList[self.channelSlotSelection].channel_Select_VAR.set("Selected") # select the new one

    def save_All_Channels_CB(self):
        print("save_All_Channels_CB called")

if __name__ == "__main__":
    root = tk.Tk()
    widget = channels(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import channelsui as baseui
from tkinter import messagebox
from configuration import configuration
import globalvars as gv


#
# Manual user code
#

class channels(baseui.channelsUI):
    channelList = []
    currentChannel = 0

    def __init__(self, master=None, mainWindow=None, refreshCallback=None, **kw):

        channels.channelList = []
        channels.currentChannel = 0
        super().__init__(master, **kw)
        self.mainWindow = mainWindow
        self.protocol("WM_DELETE_WINDOW", self.close_Channel_CB)
        self.channelSlotCount = 0
        self.channelSlotSelection = None
        self.savePreset =  int(self.mainWindow.tuning_Preset_Selection_VAR.get())
        self.mainWindow.Radio_Set_Tuning_Preset(1)
        self.refreshCallback = refreshCallback

        gv.config.register_observer("NUMBER DELIMITER", self.reformatChannelFreq)

        self.scanRunning = False
        self.scanTimer = None
        self.scanSetSelected = None
        self.scanIndex = None
        self.scanList = []



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
            child.ScanSet_Default(gv.config.get_ScanSet_Settings(self.channelSlotCount))

            self.channelSlotCount += 1
        self.scan_Select_Channel_Default()
        self.scan_Station_Time_Default()

    def reformatChannelFreq(self, new_delimiter):
        if new_delimiter  == ",":
            prior_delimiter = "."
        else:
            prior_delimiter = ","

        for child in channels.channelList:
            child.channel_Freq_VAR.set(child.channel_Freq_VAR.get().replace(prior_delimiter,new_delimiter))

        self.current_VFO_VAR.set(self.current_VFO_VAR.get().replace(prior_delimiter,new_delimiter))



    def update_Current_Frequency(self, freq):
        self.current_VFO_VAR.set(freq)

    def update_Current_Mode(self, mode):
        self.current_Mode_VAR.set(mode)


    def scan_Select_Channel_Default(self):
        self.scan_Select_Channel_VAR.set("None")

    def scan_Station_Time_Default(self):
        self.scan_Time_On_Station = gv.config.get_Scan_On_Station_Time()

    def EEPROM_SetChanneFreqMode(self, channelNum,freq, mode):

        channels.channelList[channelNum].Set_Freq(str(freq))

        channels.channelList[channelNum].Set_Mode(self.mainWindow.modeNum_To_TextDict[str(mode)])

    def EEPROM_SetChannelLabel(self, channelNum, label):
        channels.channelList[channelNum].Set_Label(label)

    def EEPROM_SetChannelShowLabel(self, channelNum, showFlag):
        channels.channelList[channelNum].Set_ShowLabel(showFlag)

    def ChannelToVFO_CB(self):               # method called when Channel->VFO

        if self.channelSlotSelection == None:
            messagebox.showinfo("Information", "Must SELECT a channel first.",
                                parent=self)
            return

        self.mainWindow.Radio_Set_New_Frequency(channels.channelList[self.channelSlotSelection].Get_Freq())
        self.mainWindow.Radio_Set_Mode(self.mainWindow.Text_To_ModeNum[channels.channelList[self.channelSlotSelection].Get_Mode()])
        self.current_Channel_VAR.set(channels.channelList[self.channelSlotSelection].Get_Label())

    def VFOToChannel_CB(self):              # method called to write current VFO to channel
        if self.channelSlotSelection == None:
            messagebox.showinfo("Information", "Must SELECT a channel first.",
                                parent=self)
            return
        channels.channelList[self.channelSlotSelection].Set_Freq(self.current_VFO_VAR.get())
        channels.channelList[self.channelSlotSelection].Set_Mode(self.current_Mode_VAR.get())
        channels.channelList[self.channelSlotSelection].channel_Dirty()

    def startScan(self):
        self.scanRunning = True
        self.scan_Channel_ButtonText_VAR.set("Stop Scan")
        self.scanIndex = 0
        self.scanList = []

        if self.scan_Select_Channel_VAR.get() == "None":
            messagebox.showinfo("Information", "Must SELECT a set of Channels to Scan before clicking the Scan Button",
                                parent=self)
            self.stopScan()
            return

        for i in range(len(channels.channelList)):
            if self.scanSetSelected == channels.channelList[i].Get_ScanSet():
                self.scanList.append(i)

        if len(self.scanList) == 0:
            messagebox.showinfo("Information", "No Channels attached to this Scan Set.",
                                parent=self)
            self.stopScan()
            return
        self.performScan()


    def performScan(self):
        self.channelSlot_CB(self.scanList[self.scanIndex])
        self.ChannelToVFO_CB()
        self.scanIndex += 1

        if self.scanIndex == len(self.scanList):
            self.scanIndex = 0
        self.scanTimer = self.master.after(self.scan_Time_On_Station, self.performScan)

    def stopScan(self):
        self.scanRunning = False
        self.scan_Channel_ButtonText_VAR.set("Run Scan")
        if self.scanTimer != None:
            self.master.after_cancel(self.scanTimer)
            self.scanTimer = None
        self.scanIndex = 0

    def scan_Channel_CB(self):              # method called to start channel scanning
        if self.scanRunning:
            self.stopScan()
        else:
            self.startScan()

    def runScan_Selection_CB(self, event=None):
        self.scanSetSelected = self.scan_Select_Channel_VAR.get()



    def refresh_Channel_CB(self):           # method called when user wants to refresh channels from EEPROM
        self.confirmExitorWriteDirty()
        self.refreshCallback()


    def close_Channel_CB(self):             # method called when window closed
        self.confirmExitorWriteDirty()
        self.mainWindow.Radio_Set_Tuning_Preset(self.savePreset)
        self.withdraw()

    def confirmExitorWriteDirty(self):
        for channelNum in range(len(self.channelList)):
            if (channels.channelList[channelNum].dirty):
                response = messagebox.askyesno("Confirmation",
                                               "Not all channels have been saved to EEPROM\nDo you want to save these channels?",
                                               parent=self)

                # Process the user's response
                if response:  # True if "Yes" is clicked
                    self.saveAllChannels_CB()
                break

    def channelSlot_CB(self, slotNumber):
        if self.channelSlotSelection != None:
            channels.channelList[self.channelSlotSelection].channel_Select_Button.configure(
                style="Button2b.TButton")
            channels.channelList[self.channelSlotSelection].channel_Select_VAR.set("Select")  # unselect the prior one

        if self.channelSlotSelection == slotNumber:         #Unselect if already selected
            self.channelSlotSelection = None
        else:
            self.channelSlotSelection = slotNumber
            channels.channelList[self.channelSlotSelection].channel_Select_Button.configure(
                    style="Button2bipressed.TButton")
            channels.channelList[self.channelSlotSelection].channel_Select_VAR.set("Selected") # select the new one

    def saveChannel(self,channelNum):
        if channelNum == None:
            messagebox.showinfo("Information", "No Channel Selected to Save",
                                parent=self)
            return
        if  (channels.channelList[channelNum].dirty):
            channels.channelList[channelNum].channel_Not_Dirty()

            self.mainWindow.Radio_Write_EEPROM_Channel_FreqMode(
                channelNum,
                channels.channelList[channelNum].Get_Freq(),
                channels.channelList[channelNum].Get_Mode())

            self.mainWindow.Radio_Write_EEPROM_Channel_Label(
                channelNum,
                channels.channelList[channelNum].Get_Label())

            self.mainWindow.Radio_Write_EEPROM_Channel_ShowLabel(
                channelNum,
                channels.channelList[channelNum].Get_ShowLabel())

            gv.config.set_ScanSet_Settings(channelNum,
                                               channels.channelList[channelNum].Get_ScanSet())


    def saveChannel_CB(self):
        self.saveChannel(self.channelSlotSelection)

    def saveAllChannels_CB(self):
        for aChannel in range(len(self.channelList)):
            self.saveChannel(aChannel)



if __name__ == "__main__":
    root = tk.Tk()
    widget = channels(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

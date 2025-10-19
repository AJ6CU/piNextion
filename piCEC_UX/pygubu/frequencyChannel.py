#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import frequencyChannelui as baseui


#
# Manual user code
#

class frequencyChannel(baseui.frequencyChannelUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.myChannelNum = 0
        self.selectCallback = None

    def assignChannelNum(self, channelNum):
        self.myChannelNum = channelNum

    def assignChannelSelect_CB(self, callback):
        self.selectCallback = callback

    def channel_Select_CB(self):
        self.selectCallback(self.myChannelNum)
    #
    #   Set up labels for channels
    #
    def channel_Number_Default(self):
        if self.myChannelNum < 9:
            self.channel_Number_VAR.set("Channel " + " "+str(int(self.myChannelNum+1)))
        else:
            self.channel_Number_VAR.set("Channel " +str(int(self.myChannelNum+1)))

    #
    #   Label get/set
    #
    def Get_Label(self):
        return self.channel_Label_VAR.get()
    def Set_Label(self, label):
        self.channel_Label_VAR.set(label)
    def Label_Default(self):
        if self.myChannelNum < 10:
            self.Set_Label("AVAIL")
        else:
            self.Set_Label("*N/A*")
            self.channel_Name_Entry.configure(state="disabled")
    #
    #   Freq get/set
    #
    def Get_Freq(self):
        return self.channel_Freq_VAR.get()
    def Set_Freq(self, freq):
        self.channel_Freq_VAR.set(freq)
    def Freq_Default(self):
        self.Set_Freq("14032000")

    #
    #   Get/Set mode combo box
    #
    def Get_Mode(self):
        return self.channel_Mode_VAR.get()
    def Set_Mode(self, mode):
        self.channel_Mode_VAR.set(mode)
    def Mode_Default(self):
        self.Set_Mode("CWU")

    #
    #   Get set show label  flag
    #
    def Get_ShowLabel(self):
        return self.channel_ShowLabel_VAR.get()
    def Set_ShowLabel(self, label):
        self.channel_ShowLabel_VAR.set(label)
    def Showlabel_Default(self):
        if self.myChannelNum < 10:
            self.Set_ShowLabel("Yes")
        else:
            self.Set_ShowLabel("No")
            self.show_Label_Combobox.configure(state="disabled")


    #
    #   Get/set Scan Set
    #
    def Get_ScanSet(self):
        return self.channel_ScanSet_VAR.get()
    def Set_ScanSet(self, scanset):
        self.channel_ScanSet_VAR.set(scanset)
    def ScanSet_Default(self):
        self.Set_ScanSet("None")












if __name__ == "__main__":
    root = tk.Tk()
    widget = frequencyChannel(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

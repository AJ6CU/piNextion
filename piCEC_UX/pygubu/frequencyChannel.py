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
    #   Label get/set
    #
    def channel_Get_Label(self):
        return self.channel_Label_VAR.get()
    def channel_Set_Label(self, label):
        self.channel_Label_VAR.set(label)
    def channel_Label_Default(self):
        if self.myChannelNum < 10:
            self.channel_Set_Label("CH0" + str(int(self.myChannelNum+1)))
        else:
            self.channel_Set_Label("*****")
            self.channel_Name_Entry.configure(state="disabled")
    #
    #   Freq get/set
    #
    def channel_Get_Freq(self):
        return self.channel_Freq_VAR.get()
    def channel_Set_Freq(self, freq):
        self.channel_Freq_VAR.set(freq)
    def channel_Freq_Default(self):
        self.channel_Set_Freq("14032000")

    #
    #   Get/Set mode combo box
    #
    def channel_Get_Mode(self):
        return self.channel_Mode_VAR.get()
    def channel_Set_Mode(self, mode):
        self.channel_Mode_VAR.set(mode)
    def select_Channel_Mode_Default(self):
        self.channel_Set_Mode("CWU")

    #
    #   Get set show label  flag
    #
    def channel_Get_ShowLabel(self):
        return self.channel_ShowLabel_VAR.get()
    def channel_Set_ShowLabel(self, label):
        self.channel_ShowLabel_VAR.set(label)
    def select_Channel_Showlabel_Default(self):
        if self.myChannelNum < 10:
            self.channel_ShowLabel_VAR.set("Yes")
        else:
            self.channel_ShowLabel_VAR.set("No")
            self.channel_Name_Entry.configure(state="disabled")
            self.show_Label_Combobox.configure(state="disabled")


    #
    #   Get/set Scan Set
    #
    def channel_Get_ScanSet(self):
        return self.channel_ScanSet_VAR.get()
    def channel_Set_ScanSet(self, scanset):
        self.channel_ScanSet_VAR.set(scanset)
    def select_ScanSet_Default(self):
        self.channel_Set_ScanSet("None")












if __name__ == "__main__":
    root = tk.Tk()
    widget = frequencyChannel(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

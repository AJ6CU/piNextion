#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import frequencyChannelui as baseui
from VirtualNumericKeyboard import VirtualNumericKeyboard
from VirtualKeyboard import VirtualKeyboard

import globalvars as gv
from tkinter import messagebox



#
# Manual user code
#

class frequencyChannel(baseui.frequencyChannelUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.myChannelNum = 0
        self.selectCallback = None
        self.dirty = False
        self.channel_label_save = None

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
        if self.myChannelNum < 9:
            self.Set_Label("AVAIL")
        else:
            self.Set_Label("*N/A*")
            self.channel_Name_Entry.configure(state="disabled")
    #
    #   Freq get/set
    #
    def Get_Freq(self):
        return gv.unformatFrequency(self.channel_Freq_VAR)
    def Set_Freq(self, freq):
        gv.formatFrequency(self.channel_Freq_VAR, freq)
    def Freq_Default(self):
        self.Set_Freq("14032000")
    #
    #   Following 2 callbacks handle both virtual and real keyboards. When a label field is clicked, the "channel_Label_Entered_CB"
    #   is called. It saves the current value, removes any blank padding on right, and then decides whether the virtual
    #   or real keyboard is to be used depending on the users' setting.
    #   If it is a virtual keyboard, then the
    #   alphanumeric_Keyboard is invoked. It takes care of error checking and padding, so there is no more work for these
    #   two routines.
    #   IF however, a real keyboard is used, then when the focus out event happens, a validation check of
    #   string length being less than 5. If greater, an error warning is generated and the string is truncated to 5.
    #   After blank padding to 5 (if needed), the entered valued is compared to the original value. If it is different,
    #   the label string is updated and it is declared "dirty"
    #

    def channel_Label_Entered_CB(self, event=None):
        self.channel_label_save = self.channel_Label_VAR.get()
        self.channel_Label_VAR.set(self.channel_label_save.replace(" ",""))
        if gv.config.get_Virtual_Keyboard_Switch() == "On":
            self.alphanumeric_Keyboard(self.channel_Label_VAR, self.channel_Name_Changed_CB, 5)

    def channel_Lavel_Validation_CB(self, p_entry_value, v_condition):
        if (v_condition == "focusout") and (gv.config.get_Virtual_Keyboard_Switch() == "Off"):
            if len(p_entry_value) > 5:
                messagebox.showinfo("Error Too Long", "Maximum of 5 characters in a channel label.\n"
                                    + "Your label has been truncated to left most 5 characters", parent=self)
                p_entry_value = p_entry_value[:5]

            p_entry_value = p_entry_value.ljust(5)          # blank pad if needed

            if (self.channel_label_save != p_entry_value):
                self.channel_Label_VAR.set(p_entry_value)
                self.channel_Dirty()
        return True

    def alphanumeric_Keyboard(self, channel_Label_strvar, change_CB, maxChars):
        keypad = VirtualKeyboard(self, channel_Label_strvar, change_CB, maxChars)

    def numeric_Keypad_CB(self, event=None):
        if gv.config.get_Virtual_Keyboard_Switch() == "On":
            keypad = VirtualNumericKeyboard(self, self.channel_Freq_VAR, self.Channel_Freq_Changed_CB,8)

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
        if self.myChannelNum < 9:
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
    def ScanSet_Default(self, value):
        self.Set_ScanSet(value)


    def channel_Dirty(self):
        if (not self.dirty):
            self.dirtyChannel_Label.configure(style="RedLED.TLabel")
            self.dirty = True

    def channel_Not_Dirty(self):
        if (self.dirty):
            self.dirtyChannel_Label.configure(style="GreenLED.TLabel")
            self.dirty = False

    def channel_Name_Changed_CB(self, event=None):
        self.channel_Dirty()

    def Channel_Freq_Changed_CB(self, event=None):
        self.channel_Dirty()

    def Channel_Mode_Changed_CB(self, event=None):
        self.channel_Dirty()

    def Channel_ShowLabel_Changed_CB(self, event=None):
        self.channel_Dirty()

    def Channel_ScanSet_Changed_CB(self, event=None):
        self.channel_Dirty()













if __name__ == "__main__":
    root = tk.Tk()
    widget = frequencyChannel(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

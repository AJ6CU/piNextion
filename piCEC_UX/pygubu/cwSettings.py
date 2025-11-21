#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import cwSettingsui as baseui
from tkinter import messagebox
import globalvars as gv


#
# Manual user code
#

class cwSettingsToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("CW Settings")
        self.popup.minsize(675,400)
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.cwSettingsWindowObj = cwSettings(self.popup, self.master, **kw)
        self.cwSettingsWindowObj.pack(expand=tk.YES, fill=tk.BOTH)

        self.cwSettingsWindowObj.loadCurrentCWSettings(self.master.tone_value_VAR.get(),
                                                       self.master.key_type_value_VAR.get(),
                                                       self.master.key_speed_value_VAR.get(),
                                                       self.master.delay_starting_tx_value_VAR.get(),
                                                       self.master.delay_returning_to_rx_value_VAR.get(),
                                                       self.master.cwTX_OffsetFlag
                                                       )


class cwSettings(baseui.cwSettingsUI):
    def __init__(self, master=None, mainWindow=None, **kw):

        self.mainWindow = mainWindow
        self.master = master
        super().__init__(self.master,  **kw)

        #
        #   Magic code to get a handle on the current font of the default item and propagate it to the list...
        #

        gv.formatCombobox( self.CW_Display_Freq_Combobox, "Arial", "24", "bold")

        self.orig_tone = None
        self.orig_key_type = None
        self.orig_keySpeed = None
        self.delay_starting_tx = None
        self.delay_returning_to_rx = None
        self.offset_Freq_Flag = None


    def loadCurrentCWSettings(self,tone,keyType,keySpeed,delayToTX,delayToRX, offset_Freq_Flag):
        #
        #   Save originals for dirty testing later
        #
        self.orig_tone = tone
        self.orig_key_type = keyType
        self.orig_keySpeed = keySpeed
        self.delay_starting_tx = delayToTX
        self.delay_returning_to_rx = delayToRX
        self.offset_Freq_Flag = offset_Freq_Flag
        #
        #   Stuff values into stringvars of the UX
        #
        self.tone_value_VAR.set(tone)
        self.key_type_value_VAR.set(keyType)
        self.key_speed_value_VAR.set(keySpeed)
        self.delay_starting_tx_value_VAR.set(delayToTX)
        self.delay_returning_to_rx_value_VAR.set(delayToRX)
        if self.offset_Freq_Flag:
            self.CW_Display_TXFreq_VAR.set("TX")
        else:
            self.CW_Display_TXFreq_VAR.set("RX")


    def dirty_DisplayCWSettings (self):
        reboot_required = False
        if( self.tone_value_VAR.get() != self.orig_tone):
            self.mainWindow.Radio_Set_CW_Tone(self.tone_value_VAR.get())
            reboot_required = True

        if (self.key_type_value_VAR.get() != self.orig_key_type):
            self.mainWindow.Radio_Set_CW_Keytype(self.key_type_value_VAR.get())

        if (self.key_speed_value_VAR.get() != self.orig_keySpeed):
            self.mainWindow.Radio_Set_CW_Speed(self.key_speed_value_VAR.get())

        if (self.delay_starting_tx_value_VAR.get() != self.delay_starting_tx):
            self.mainWindow.Radio_Set_CW_Delay_Starting_TX(self.delay_starting_tx_value_VAR.get())
            reboot_required = True

        if (self.delay_returning_to_rx_value_VAR.get() != self.delay_returning_to_rx):
            self.mainWindow.Radio_Set_CW_Delay_Returning_To_RX(self.delay_returning_to_rx_value_VAR.get())
            reboot_required = True
        #
        #   Note: self.offset_Freq_Flag should generally be the sames as self.mainWindow.cwTX_OffsetFlag
        #   However, there could be a case where a delayed setting by the MCU comes after the CW settings
        #   is displayed causing a race condition. THis is the logic for using the saved value
        #
        if (self.CW_Display_TXFreq_VAR.get()) == 'RX' and self.offset_Freq_Flag:
            self.mainWindow.cwTX_OffsetFlag = False
            self.mainWindow.offsetVFOforTX(False)
        elif (self.CW_Display_TXFreq_VAR.get()) == 'TX' and not self.offset_Freq_Flag:
            self.mainWindow.cwTX_OffsetFlag = True
            self.mainWindow.offsetVFOforTX(True)



        if(reboot_required):
            response = messagebox.askyesno("Reboot Required", "One or more changes require a reboot to take effect.\n\n"+
                                           "Do you want to reboot now?",
                                            parent=self, icon="warning")
            if response:
                self.mainWindow.theRadio.rebootRadio()
            else:
                print('told us to wait')




    def apply_CB(self):
        self.dirty_DisplayCWSettings()
        self.master.destroy()

    def cancel_CB(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = cwSettings(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

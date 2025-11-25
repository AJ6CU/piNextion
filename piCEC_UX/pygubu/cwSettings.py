#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import cwSettingsui as baseui
from tkinter import messagebox
import globalvars as gv
from time import sleep


#
# Manual user code
#

class cwSettingsToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("CW Settings")
        self.popup.minsize(800,500)
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

        gv.formatCombobox(self.CW_Keytype_Widget_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.CW_Sidetone_Widget_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.CW_Speed_WPM_Widget_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.CW_Start_MS_Widget_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.CW_Delay_MS_Widget_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.CW_Display_Freq_Combobox, "Arial", "24", "bold")


        self.CW_Sidetone_Widget_Combobox.configure(values=gv.CW_Sidetone_Values)
        self.CW_Speed_WPM_Widget_Combobox.configure(values=gv.CW_WPM_Values)
        self.CW_Start_MS_Widget_Combobox.configure(values=gv.Start_TX_Values)
        self.CW_Delay_MS_Widget_Combobox.configure(values=gv.Delay_Return_RX_Values)


        self.orig_tone = None
        self.orig_key_type = None
        self.orig_keySpeed = None
        self.delay_starting_tx = None
        self.delay_returning_to_rx = None
        self.offset_Freq_Flag = None

        #
        # the following is a failed attempt to get the combobox to scroll the selected value to the middle of the list
        # perhaps I will figure this out in the future....
        #

    # def combobox_center_list_CB(self):
    #
    #     """Scrolls the listbox to the currently selected item."""
    #     # Get the index of the current value
    #     print(" trying to scroll the listbox")
    #
    #     try:
    #         current_index = gv.CW_Sidetone_Values.index(self.tone_value_VAR.get())
    #     except:             # not found just return
    #         print(" value not in list")
    #         return
    #
    #     # Access the internal Tcl/Tk listbox widget
    #     try:
    #         # This is a non-public method, subject to change across Tk versions
    #         # It returns the Tk widget name for the internal listbox
    #         # listbox_name = self.tk.call(self._w, "listbox")
    #         # print("failed on first call")
    #         # listbox = self.winfo_toplevel().nametowidget(listbox_name)
    #         print("trying to find popdown widget")
    #         popdown_window = self.master.tk.call(
    #             "ttk::combobox::PopdownWindow", self.master._w
    #         )
    #         print("got thru popdown window")
    #         # The listbox is inside a frame named ".f", and its name is ".l"
    #         listbox_path = popdown_window + ".f.l"
    #         print("found path", listbox_path)
    #         # Get the Python widget reference using the path
    #         modpath = ".!root"+listbox_path
    #         print("modpath", modpath)
    #         listbox = self.nametowidget(modpath)
    #         print("found listbox")
    #
    #         # Use the see() method to ensure the current item is visible
    #         # The listbox will scroll to show the index
    #         print("got to the see")
    #         listbox.see(current_index)
    #         print("failed on see")
    #
    #         # To try and "center" it more, you could calculate an offset
    #         # For this example, 'see' ensures visibility
    #
    #     except:
    #         print("failed to access internal")
    #         return          # can't access internal, just dont try to center the list


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
                sleep (1.5)              # sleep a little so that the change to settings are processed before reboot
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

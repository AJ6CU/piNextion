#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsBackupui as baseui
from configuration import configuration
import globalvars as gv
from time import sleep


#
# Manual user code
#

class settingsBackupToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Radio Backup/Restore")
        self.popup.geometry("600x430")
        self.popup.wait_visibility()  # required on Linux
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsBackupWindow = settingsBackup(self.popup, self.master, **kw)
        self.settingsBackupWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsBackup(baseui.settingsBackupUI):
    def __init__(self, master=None,mainWindow=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow

        self.ConfigFile_Master_Cal_VAR.set(gv.config.get_Master_Cal())
        self.ConfigFile_SSB_BFO_VAR.set(gv.config.get_SSB_BFO())
        self.ConfigFIle_CW_BFO_VAR.set(gv.config.get_CW_BFO())

        gv.formatCombobox(self.action_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.from_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.to_Combobox, "Arial", "24", "bold")

        self.action_Combobox_VAR.set("Select")
        self.from_Combobox_VAR.set("Select")
        self.to_Combobox_VAR.set("Select")



        mainWindow.Radio_Req_Master_Cal(self.set_Master_Cal)
        mainWindow.Radio_Req_SSB_BFO(self.set_SSB_BFO)
        mainWindow.Radio_Req_CW_BFO(self.set_CW_BFO)
        mainWindow.Radio_Req_Factory_Master_Cal(self.set_Factory_Master_Cal)
        mainWindow.Radio_Req_Factory_SSB_BFO(self.set_Factory_SSB_BFO)
        sleep(.5)

    def set_Master_Cal(self, value):
        self.EEPROM_Current_Master_Cal_VAR.set(value)

    def set_SSB_BFO(self, value):
        self.EEPROM_Current_SSB_BFO_VAR.set(value)

    def set_CW_BFO(self, value):
        self.EEPROM_Current_CW_BFO_VAR.set(value)

    def set_Factory_Master_Cal(self, value):
        self.EEPROM_Factory_Master_Cal_VAR.set(value)

    def set_Factory_SSB_BFO(self, value):
        self.EEPROM_Factory_SSB_BFO_VAR.set(value)



    def apply_CB(self):
        print("Applying settings")

        # if int(self.MCU_Command_Headroom_VAR.get()) != self.saveMCU_Command_Headroom:
        #     gv.config.set_MCU_Command_Headroom(int(self.MCU_Command_Headroom_VAR.get())/1000)
        #
        #
        # if int(self.MCU_Update_Period_VAR.get()) != self.saveMCU_Update_Period:
        #     gv.config.set_MCU_Update_Period(int(self.MCU_Update_Period_VAR.get()))

        self.master.destroy()

    def cancel_CB(self):
        print("Cancelling settings")
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsBackup(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

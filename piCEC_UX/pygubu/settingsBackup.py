#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsBackupui as baseui
from configuration import configuration
import globalvars as gv


#
# Manual user code
#

class settingsBackupToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Radio Backup/Restore")
        self.popup.geometry("600x430")
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsBackupWindow = settingsBackup(self.popup, self.master, **kw)
        self.settingsBackupWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsBackup(baseui.settingsBackupUI):
    def __init__(self, master=None,mainWindow=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow

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

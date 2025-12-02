#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsui as baseui
import settingsMachine as sm
from cwSettings import cwSettingsToplevel
from settingsMachine import settingsMachineToplevel
from settingsMisc import settingsMiscToplevel
from settingsBackup import settingsBackupToplevel
from settingsFactoryReset import settingsFatoryResetToplevel
from tkinter import messagebox


#
# Manual user code
#


class settingsToplevel(tk.Toplevel):
    def __init__(self, master=None,  **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("PiCEC Software Settings")
        self.popup.geometry("600x425")
        self.popup.wait_visibility()  # required on Linux
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsWindowObj = settings(self.popup,  self.master, **kw)
        self.settingsWindowObj.pack(expand=tk.YES, fill=tk.BOTH)


class settings(baseui.settingsUI):
    def __init__(self, master=None, mainWindow = None,  **kw):
        self.master = master
        self.mainWindow = mainWindow

        super().__init__(self.master, **kw)
        self.master.protocol("WM_DELETE_WINDOW", self.settingsClose_CB)


        self.settingsMachineWindow = None


        self.settingsCWWindow = None


        self.settingsMiscWindow = None


        self.settingsChannelsWindow = None

        self.settingsBackupWindow = None


        self.settingsFactoryResetWindow = None

        self.settingsRebootWindow = None



    def settingsClose_CB(self):
        self.master.destroy()

    def SettingsMachine_CB(self):
        self.settingsMachineWindow = settingsMachineToplevel(self.mainWindow)

    def settingsCW_CB(self):
        self.settingsCWWindow = cwSettingsToplevel(self.mainWindow)


    def settingsMisc_CB(self):
        self.settingsMiscWindow = settingsMiscToplevel(self.mainWindow)

    def settingsBackup_CB(self):
        self.settingsBackupWindow = settingsBackupToplevel(self.mainWindow)

    def settingsReboot_CB(self):
        if messagebox.askokcancel("Reboot?", "Do you really want to reboot?", parent=self):
            self.mainWindow.theRadio.rebootRadio()




if __name__ == "__main__":
    root = tk.Tk()
    widget = settings(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

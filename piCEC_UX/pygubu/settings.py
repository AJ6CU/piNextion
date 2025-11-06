#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsui as baseui
import settingsMachine as sm


#
# Manual user code
#

class settings(baseui.settingsUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.settingsClose_CB)

        self.settingsMachineWindowObj = None
        self.settingsMachineWindow = None

        self.settingsCWWindowObj = None
        self.settingsCWWindow = None

        self.settingsMiscWindowObj = None
        self.settingsMiscWindow = None

        self.settingsChannelsWindowObj = None
        self.settingsChannelsWindow = None

        self.settingsBackupWindowObj = None
        self.settingsBackupWindow = None

        self.settingsFactoryResetWindowObj = None
        self.settingsFactoryResetWindow = None

        self.settingsRebootWindowObj = None
        self.settingsRebootWindow = None



    def settingsClose_CB(self):
        self.master.destroy()

    def SettingsMachine_CB(self):
        self.settingsMachineWindow = tk.Toplevel(self.master)
        self.settingsMachineWindow.title("Machine Settings")
        self.settingsMachineWindow.geometry("400x320")

        self.settingsMachineWindowObj = sm.settingsMachine(self.settingsMachineWindow)
        self.settingsMachineWindowObj.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsMachineWindow.grab_set()
        self.settingsMachineWindow.transient(self)  # Makes the Classic box appear above the mainwindow

    def settingsCW_CB(self):
        self.settingsCWWindow = tk.Toplevel(self.master)
        self.settingsCWWindow.title("Machine Settings")
        self.settingsCWWindow.geometry("400x320")

        self.settingsCWWindowObj = cw.settingsMachine(self.settingsMachineWindow)
        self.settingsCWWindow.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsCWWindow.grab_set()
        self.settingsCWWindow.transient(self)  # Makes the Classic box appear above the mainwindow

    def settingsMisc_CB(self):
        self.settingsMachineWindow = tk.Toplevel(self.master)
        self.settingsMachineWindow.title("Machine Settings")
        self.settingsMachineWindow.geometry("400x320")

        self.settingsMachineWindowObj = sm.settingsMachine(self.settingsMachineWindow)
        self.settingsMachineWindowObj.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsMachineWindow.grab_set()
        self.settingsMachineWindow.transient(self)  # Makes the Classic box appear above the mainwindow

    def settingsChannels_CB(self):
        self.settingsMachineWindow = tk.Toplevel(self.master)
        self.settingsMachineWindow.title("Machine Settings")
        self.settingsMachineWindow.geometry("400x320")

        self.settingsMachineWindowObj = sm.settingsMachine(self.settingsMachineWindow)
        self.settingsMachineWindowObj.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsMachineWindow.grab_set()
        self.settingsMachineWindow.transient(self)  # Makes the Classic box appear above the mainwindow

    def settingsBackup_CB(self):
        self.settingsMachineWindow = tk.Toplevel(self.master)
        self.settingsMachineWindow.title("Machine Settings")
        self.settingsMachineWindow.geometry("400x320")

        self.settingsMachineWindowObj = sm.settingsMachine(self.settingsMachineWindow)
        self.settingsMachineWindowObj.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsMachineWindow.grab_set()
        self.settingsMachineWindow.transient(self)  # Makes the Classic box appear above the mainwindow

    def settingsFactoryReset_CB(self):
        self.settingsMachineWindow = tk.Toplevel(self.master)
        self.settingsMachineWindow.title("Machine Settings")
        self.settingsMachineWindow.geometry("400x320")

        self.settingsMachineWindowObj = sm.settingsMachine(self.settingsMachineWindow)
        self.settingsMachineWindowObj.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsMachineWindow.grab_set()
        self.settingsMachineWindow.transient(self)  # Makes the Classic box appear above the mainwindow

    def settingsReboot_CB(self):
        self.settingsMachineWindow = tk.Toplevel(self.master)
        self.settingsMachineWindow.title("Machine Settings")
        self.settingsMachineWindow.geometry("400x320")

        self.settingsMachineWindowObj = sm.settingsMachine(self.settingsMachineWindow)
        self.settingsMachineWindowObj.pack(expand=tk.YES, fill=tk.BOTH)
        self.settingsMachineWindow.grab_set()
        self.settingsMachineWindow.transient(self)  # Makes the Classic box appear above the mainwindow



if __name__ == "__main__":
    root = tk.Tk()
    widget = settings(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

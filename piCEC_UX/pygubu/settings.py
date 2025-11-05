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



if __name__ == "__main__":
    root = tk.Tk()
    widget = settings(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

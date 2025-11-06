#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsMachineui as baseui
from configuration import configuration
import globalvars as gv


#
# Manual user code
#
class settingsMachineToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Machine Specific Settings")
        self.popup.geometry("600x430")
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsMachineWindow = settingsMachine(self.popup, self.master, **kw)
        self.settingsMachineWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsMachine(baseui.settingsMachineUI):
    def __init__(self, master=None, mainWindow=None, **kw):
        self.master = master
        self.mainWindow = mainWindow

        super().__init__(master, **kw)
        print(gv.config.get_Advanced_Settings("MCU Command Headroom"))

    def apply_CB(self):
        print("Applying settings")
        self.master.destroy()

    def cancel_CB(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsMachine(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

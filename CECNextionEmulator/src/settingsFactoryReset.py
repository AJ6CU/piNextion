#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsFactoryResetui as baseui
from configuration import configuration
import globalvars as gv


#
# Manual user code
#

#
# Manual user code
#
class settingsFatoryResetToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Reset to Factory Settings")
        self.popup.geometry("600x430")
        self.popup.wait_visibility()  # required on Linux
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsFactoryResetWindow = settingsFactoryReset(self.popup, self.master, **kw)
        self.settingsFactoryResetWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsFactoryReset(baseui.settingsFactoryResetUI):
    def __init__(self, master=None, mainWindow=None, **kw):
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
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsFactoryReset(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

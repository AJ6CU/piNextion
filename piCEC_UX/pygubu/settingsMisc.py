#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsMiscui as baseui
from configuration import configuration
import globalvars as gv


#
# Manual user code
#

class settingsMiscToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Misc Settings")
        self.popup.geometry("600x430")
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsMiscWindow = settingsMisc(self.popup, self.master, **kw)
        self.settingsMiscWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsMisc(baseui.settingsMiscUI):
    def __init__(self, master=None, mainWindow=None, **kw):
        self.master = master
        self.mainWindow = mainWindow

        super().__init__(master, **kw)

        self.saveNumber_Delimiter = gv.config.get_Number_Delimiter()
        self.Number_Delimiter_VAR.set(self.saveNumber_Delimiter)

    def apply_CB(self):
        print("Applying settings")

        if self.Number_Delimiter_VAR.get() != self.saveNumber_Delimiter:
            gv.config.set_Number_Delimiter(self.Number_Delimiter_VAR.get())

        self.master.destroy()

    def cancel_CB(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsMisc(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

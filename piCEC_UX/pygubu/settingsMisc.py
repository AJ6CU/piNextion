#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

import tkinter.font as font
import tkinter.font as tkFont

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
        self.popup.wait_visibility()  # required on Linux
        self.popup.grab_set()
        self.popup.transient(self.master)

        # bigfont = tkFont.Font(family="Helvetica", size=48)
        # self.popup.option_add("*TCombobox*Listbox*Font", bigfont)

        self.settingsMiscWindow = settingsMisc(self.popup, self.master, **kw)
        self.settingsMiscWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsMisc(baseui.settingsMiscUI):
    def __init__(self, master=None, mainWindow=None, **kw):
        self.master = master
        self.mainWindow = mainWindow

        super().__init__(master, **kw)

#
        #
        #   Magic code to get a handle on the current font of the default item and propagate it to the list...
        #

        gv.formatCombobox( self.Number_Delimiter_Combobox, "Arial", "36", "bold")

        self.saveNUMBER_DELIMITER = gv.config.get_NUMBER_DELIMITER()
        self.NUMBER_DELIMITER_VAR.set(self.saveNUMBER_DELIMITER)

    def apply_CB(self):
        print("Applying settings")

        if self.NUMBER_DELIMITER_VAR.get() != self.saveNUMBER_DELIMITER:
            gv.config.set_NUMBER_DELIMITER(self.NUMBER_DELIMITER_VAR.get())

        self.master.destroy()

    def cancel_CB(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsMisc(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

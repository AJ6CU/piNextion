#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import cwSettingsui as baseui


#
# Manual user code
#

class cwSettings(baseui.cwSettingsUI):
    def __init__(self, master=None, mainWindow=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow

    def setDirtyCB(self, dirty_CB):
        self.dirty_CB = dirty_CB

    def apply_CB(self):
        print("outside apply CB")
        self.mainWindow.dirty_DisplayCWSettings()
        self.destroy()

    def cancel_CB(self):
        print("outside cancel CB")
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = cwSettings(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

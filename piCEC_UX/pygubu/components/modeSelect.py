#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import components.modeSelectui as baseui


#
# Manual user code
#

class modeSelect(baseui.modeSelectUI):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        # we need the parent for runing in modal mode
        self.parent = master
        self.hide()
        
    # def show(self):


    def hide(self):
        self.withdraw()


if __name__ == "__main__":
    root = tk.Tk()
    widget = modeSelect(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

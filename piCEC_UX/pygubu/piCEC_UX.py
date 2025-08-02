#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import piCEC_UXui as baseui

import mystyles  # Styles definition module

# PROJECT_PATH = pathlib.Path(__file__).parent
# PROJECT_UI = "piCEC_UX.ui"
# RESOURCE_PATHS = [PROJECT_PATH]


#
# Manual user code
#

class piCECNextion(baseui.piCECNextionUI):
    def __init__(self, master=None, **kw):
        super().__init__(
            master,
            translator=None,
            on_first_object_cb=mystyles.setup_ttk_styles
        )


if __name__ == "__main__":
    root = tk.Tk()
    widget = piCECNextion(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

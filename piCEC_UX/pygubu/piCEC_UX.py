     #!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from piCEC_UXui import piCECNextionUI
import mystyles  # Styles definition module


class piCECNextion(piCECNextionUI):
    def __init__(self, master=None, on_first_object_cb=None):
        super().__init__(master, on_first_object_cb=mystyles.setup_ttk_styles)


if __name__ == "__main__":
    app = piCECNextion()
    app.run()

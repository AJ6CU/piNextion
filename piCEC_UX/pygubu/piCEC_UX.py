#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from piCEC_UXui import piCECNextionUI
import mystyles  # Styles definition module

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "piCEC_UX.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class piCECNextion(piCECNextionUI):
    def __init__(self, master=None):
        super().__init__(
            master,
            project_ui=PROJECT_UI,
            resource_paths=RESOURCE_PATHS,
            translator=None,
            on_first_object_cb=mystyles.setup_ttk_styles
        )


if __name__ == "__main__":
    app = piCECNextion()
    app.run()

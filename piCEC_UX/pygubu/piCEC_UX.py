#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from piCEC_UXui import piCECNextionUI
import mystyles  # Styles definition module
# from components.modeSelect import modeSelect

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
        # self.modeMenu = None


    def settings_CB():
        pass

    def vfo_CB(self):
        pass

    def show_mode(self):
        pass

    def mode_CB(self):
        print("mode callback")
        # self.modeMenu = modeSelect(self.mainwindow)
        grid_remove(vfo_display_Frame)


    def band_up_CB(self):
        pass

    def band_dn_CB(self):
        pass

    def lock_CB(self):
        pass

    def speaker_CB(self):
        pass

    def stop_CB(self):
        pass

    def tuning_Step_CB(self):
        pass

    def split_CB(self):
        pass

    def rit_CB(self):
        pass

    def store_CB(self):
        pass

    def recall_CB(self):
        pass

    def att_CB(self):
        pass

    def ifs_CB(self):
        pass


if __name__ == "__main__":
    app = piCECNextion()
    app.run()

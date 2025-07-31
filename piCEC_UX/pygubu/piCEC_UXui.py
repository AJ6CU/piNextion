#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu


class piCECNextionUI:
    def __init__(
        self,
        master=None,
        *,
        project_ui,
        resource_paths=None,
        translator=None,
        on_first_object_cb=None,
        data_pool=None,
    ):
        self.builder = pygubu.Builder(
            translator=translator,
            on_first_object=on_first_object_cb,
            data_pool=data_pool
        )
        self.builder.add_from_file(project_ui)
        if resource_paths is not None:
            self.builder.add_resource_paths(resource_paths)
        # Main widget
        self.mainwindow: tk.Tk = self.builder.get_object("main_window", master)
        self.builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

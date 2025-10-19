#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.combobox import Combobox


def i18n_translator_noop(value):
    """i18n - Setup translator in derived class file"""
    return value


def first_object_callback_noop(widget):
    """on first objec callback - Setup callback in derived class file."""
    pass


def image_loader_default(master, image_name: str):
    """Image loader - Setup image_loader in derived class file."""
    img = None
    try:
        img = tk.PhotoImage(file=image_name, master=master)
    except tk.TclError:
        pass
    return img


#
# Base class definition
#
class frequencyChannelUI(ttk.Frame):
    def __init__(
        self,
        master=None,
        *,
        translator=None,
        on_first_object_cb=None,
        data_pool=None,
        image_loader=None,
        **kw
    ):
        if translator is None:
            translator = i18n_translator_noop
        _ = translator  # i18n string marker.
        if image_loader is None:
            image_loader = image_loader_default
        if on_first_object_cb is None:
            on_first_object_cb = first_object_callback_noop

        super().__init__(master, **kw)

        self.channel_Select_Button = ttk.Button(
            self, name="channel_select_button")
        self.channel_Select_VAR = tk.StringVar(value='Select')
        self.channel_Select_Button.configure(
            style="Button2b.TButton",
            text='Select',
            textvariable=self.channel_Select_VAR)
        # First object created
        on_first_object_cb(self.channel_Select_Button)

        self.channel_Select_Button.grid(column=0, row=0)
        self.channel_Select_Button.configure(command=self.channel_Select_CB)
        self.channel_Name_Entry = ttk.Entry(self, name="channel_name_entry")
        self.channel_Label_VAR = tk.StringVar()
        self.channel_Name_Entry.configure(
            justify="left",
            style="Normal.TEntry",
            textvariable=self.channel_Label_VAR,
            width=5)
        self.channel_Name_Entry.grid(column=1, padx="10 0", row=0, sticky="w")
        self.freq_Label = ttk.Label(self, name="freq_label")
        self.channel_Freq_VAR = tk.StringVar()
        self.freq_Label.configure(
            anchor="w",
            style="Heading2b.TLabel",
            textvariable=self.channel_Freq_VAR,
            width=10)
        self.freq_Label.grid(column=2, padx="10 0", row=0, sticky="w")
        self.mode_Combobox = Combobox(self, name="mode_combobox")
        self.channel_Mode_VAR = tk.StringVar()
        self.mode_Combobox.configure(
            justify="center",
            keyvariable=self.channel_Mode_VAR,
            state="normal",
            style="ComboBox2b.TCombobox",
            values='Default LSB USB CWL CWU',
            width=8)
        self.mode_Combobox.grid(column=3, padx="10 0", row=0)
        self.show_Label_Combobox = Combobox(self, name="show_label_combobox")
        self.channel_ShowLabel_VAR = tk.StringVar()
        self.show_Label_Combobox.configure(
            justify="center",
            keyvariable=self.channel_ShowLabel_VAR,
            state="normal",
            style="ComboBox2b.TCombobox",
            values='Yes No',
            width=5)
        self.show_Label_Combobox.grid(column=4, padx="10 0", row=0)
        self.scan_Set_Combobox = Combobox(self, name="scan_set_combobox")
        self.channel_ScanSet_VAR = tk.StringVar()
        self.scan_Set_Combobox.configure(
            justify="center",
            keyvariable=self.channel_ScanSet_VAR,
            state="normal",
            style="ComboBox2b.TCombobox",
            values='None Scan1 Scan2 Scan3 Scan4',
            width=5)
        self.scan_Set_Combobox.grid(column=5, padx="10 0", row=0)
        self.configure(height=200, style="Normal.TFrame", width=200)
        # Layout for 'frequencyChannel' skipped in custom widget template.

    def channel_Select_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = frequencyChannelUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

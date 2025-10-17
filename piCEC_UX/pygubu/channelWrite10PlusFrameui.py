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
class channelWrite10PlusFrameUI(ttk.Frame):
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

        self.mem_Write_Select_Button = ttk.Button(
            self, name="mem_write_select_button")
        self.mem_Channel_Select_VAR = tk.StringVar(value='Select')
        self.mem_Write_Select_Button.configure(
            style="Button2b.TButton",
            text='Select',
            textvariable=self.mem_Channel_Select_VAR)
        # First object created
        on_first_object_cb(self.mem_Write_Select_Button)

        self.mem_Write_Select_Button.grid(column=0, row=0)
        self.mem_Write_Select_Button.configure(
            command=self.mem_Select_Write_CB)
        self.freq_Label = ttk.Label(self, name="freq_label")
        self.Freq_VAR = tk.StringVar(value='99.999.999')
        self.freq_Label.configure(
            style="Heading2b.TLabel",
            text='99.999.999',
            textvariable=self.Freq_VAR)
        self.freq_Label.grid(column=2, padx="10 0", row=0)
        self.mode_Combobox = Combobox(self, name="mode_combobox")
        self.Mode_VAR = tk.StringVar()
        self.mode_Combobox.configure(
            keyvariable=self.Mode_VAR,
            state="normal",
            style="ComboBox2b.TCombobox",
            values='Default LSB USB CWL CWU',
            width=8)
        self.mode_Combobox.grid(column=3, padx="10 0", row=0)
        self.mode_Combobox.configure(
            postcommand=self.select_Channel_Mode_Default)
        self.show_Label_Combobox = Combobox(self, name="show_label_combobox")
        self.showLabel_VAR = tk.StringVar()
        self.show_Label_Combobox.configure(
            keyvariable=self.showLabel_VAR,
            state="normal",
            style="ComboBox2b.TCombobox",
            values='Yes No',
            width=5)
        self.show_Label_Combobox.grid(column=4, padx="10 0", row=0)
        self.show_Label_Combobox.configure(
            postcommand=self.select_Channel_Showlabel_Default)
        self.Label = ttk.Label(self, name="label")
        self.Label_VAR = tk.StringVar(value='Channel 11')
        self.Label.configure(
            state="normal",
            style="Heading2bi.TLabel",
            text='Channel 11',
            textvariable=self.Label_VAR,
            width=12)
        self.Label.grid(column=1, padx="10 0", row=0)
        self.configure(height=200, style="Normal.TFrame", width=200)
        # Layout for 'channelWrite10Plus' skipped in custom widget template.

    def mem_Select_Write_CB(self):
        pass

    def select_Channel_Mode_Default(self):
        pass

    def select_Channel_Showlabel_Default(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelWrite10PlusFrameUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

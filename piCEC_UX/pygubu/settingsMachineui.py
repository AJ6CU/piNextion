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
class settingsMachineUI(ttk.Labelframe):
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

        frame1 = ttk.Frame(self)
        frame1.configure(height=200, style="Normal.TFrame", width=200)
        # First object created
        on_first_object_cb(frame1)

        self.MCU_Command_Headroom_Label = ttk.Label(
            frame1, name="mcu_command_headroom_label")
        self.MCU_Command_Headroom_Label.configure(
            style="Heading1b.TLabel",
            text='Minimum time between\ncommands sent to\nRadio (ms):')
        self.MCU_Command_Headroom_Label.grid(
            column=0, padx=10, pady=10, row=0, sticky="e")
        self.MCU_Command_Headroom_Combobox = Combobox(
            frame1, name="mcu_command_headroom_combobox")
        self.MCU_Command_Headroom_VAR = tk.StringVar()
        self.MCU_Command_Headroom_Combobox.configure(
            keyvariable=self.MCU_Command_Headroom_VAR,
            style="ComboBox1.TCombobox",
            values='90 100',
            width=4)
        self.MCU_Command_Headroom_Combobox.grid(
            column=1, padx=20, pady=10, row=0)
        self.MCU_Update_Period_Label = ttk.Label(
            frame1, name="mcu_update_period_label")
        self.MCU_Update_Period_Label.configure(
            style="Heading1b.TLabel",
            text='Frequency to check for\nUX changes (ms):')
        self.MCU_Update_Period_Label.grid(
            column=0, padx=10, pady=50, row=1, sticky="e")
        self.MCU_Update_Period_Combobox = Combobox(
            frame1, name="mcu_update_period_combobox")
        self.MCU_Update_Period_VAR = tk.StringVar()
        self.MCU_Update_Period_Combobox.configure(
            keyvariable=self.MCU_Update_Period_VAR,
            style="ComboBox1.TCombobox",
            values='500 600',
            width=4)
        self.MCU_Update_Period_Combobox.grid(column=1, padx=20, pady=50, row=1)
        frame1.pack(padx=10, pady=10, side="top")
        self.closingFrame = ttk.Frame(self, name="closingframe")
        self.closingFrame.configure(
            height=50, style="Normal.TFrame", width=200)
        self.apply_Button = ttk.Button(self.closingFrame, name="apply_button")
        self.apply_Button.configure(style="Button2b.TButton", text='Apply')
        self.apply_Button.pack(anchor="center", padx=10, side="left")
        self.apply_Button.configure(command=self.apply_CB)
        self.cancel_Buttom = ttk.Button(
            self.closingFrame, name="cancel_buttom")
        self.cancel_Buttom.configure(style="Button2b.TButton", text='Cancel')
        self.cancel_Buttom.pack(anchor="center", padx=10, side="left")
        self.cancel_Buttom.configure(command=self.cancel_CB)
        self.closingFrame.pack(
            anchor="center",
            expand=False,
            pady=20,
            side="top")
        self.configure(
            height=400,
            style="Heading2.TLabelframe",
            text='Advanced Settings',
            width=600)
        # Layout for 'labelframe1' skipped in custom widget template.

    def apply_CB(self):
        pass

    def cancel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsMachineUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

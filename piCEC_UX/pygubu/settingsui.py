#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


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
class settingsUI(ttk.Labelframe):
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

        self.settingsButtons_Frame = ttk.Frame(
            self, name="settingsbuttons_frame")
        self.settingsButtons_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        # First object created
        on_first_object_cb(self.settingsButtons_Frame)

        self.settingsMachine_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsmachine_button")
        self.settingsMachine_Button.configure(
            style="Button1Raised.TButton", text='Machine', width=14)
        self.settingsMachine_Button.grid(
            column=0, ipady=25, padx=10, pady=10, row=0)
        self.settingsMachine_Button.configure(command=self.SettingsMachine_CB)
        self.settingsCW_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingscw_button")
        self.settingsCW_Button.configure(
            style="Button1Raised.TButton",
            text='CW Settings',
            width=14)
        self.settingsCW_Button.grid(
            column=1, ipady=25, padx=10, pady=10, row=0)
        self.settingsCW_Button.configure(command=self.settingsCW_CB)
        self.settingsMisc_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsmisc_button")
        self.settingsMisc_Button.configure(
            style="Button1Raised.TButton", text='Misc', width=14)
        self.settingsMisc_Button.grid(
            column=2, ipady=25, padx=10, pady=10, row=0)
        self.settingsMisc_Button.configure(command=self.settingsMisc_CB)
        self.settingsChannels = ttk.Button(
            self.settingsButtons_Frame, name="settingschannels")
        self.settingsChannels.configure(
            style="Button1Raised.TButton", text='Channels', width=14)
        self.settingsChannels.grid(column=0, ipady=25, padx=10, pady=10, row=2)
        self.settingsChannels.configure(command=self.settingsChannels_CB)
        self.settingsBackup_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsbackup_button")
        self.settingsBackup_Button.configure(
            style="Button1Raised.TButton", text='Backup', width=14)
        self.settingsBackup_Button.grid(
            column=1, ipady=25, padx=10, pady=10, row=2)
        self.settingsBackup_Button.configure(command=self.settingsBackup_CB)
        self.settingsReserved2_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsreserved2_button")
        self.settingsReserved2_Button.configure(
            state="disabled", style="Button1Raised.TButton", text='tbd', width=14)
        self.settingsReserved2_Button.grid(
            column=2, ipady=25, padx=10, pady=10, row=2)
        self.settingsFactoryReset_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsfactoryreset_button")
        self.settingsFactoryReset_Button.configure(
            style="Button1Raised.TButton", text='Factory Reset', width=14)
        self.settingsFactoryReset_Button.grid(
            column=1, ipady=25, padx=10, pady=10, row=3)
        self.settingsFactoryReset_Button.configure(
            command=self.settingsFactoryReset_CB)
        self.settingsReboot_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsreboot_button")
        self.settingsReboot_Button.configure(
            style="Button1Raised.TButton", text='Reboot uBITX', width=14)
        self.settingsReboot_Button.grid(
            column=0, ipady=25, padx=10, pady=10, row=3)
        self.settingsReboot_Button.configure(command=self.settingsReboot_CB)
        self.settingsReserved3_Button = ttk.Button(
            self.settingsButtons_Frame, name="settingsreserved3_button")
        self.settingsReserved3_Button.configure(
            state="disabled", style="Button1Raised.TButton", text='tbd', width=14)
        self.settingsReserved3_Button.grid(
            column=2, ipady=25, padx=10, pady=10, row=3)
        self.settingsButtons_Frame.pack(
            anchor="center", expand=True, fill="both", side="top")
        self.settingsClose_Frame = ttk.Frame(self, name="settingsclose_frame")
        self.settingsClose_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.settingsClosed_Button = ttk.Button(
            self.settingsClose_Frame, name="settingsclosed_button")
        self.settingsClosed_Button.configure(
            style="Button1Raised.TButton", text='Close')
        self.settingsClosed_Button.pack(anchor="center", ipady=5, side="top")
        self.settingsClosed_Button.configure(command=self.settingsClose_CB)
        self.settingsClose_Frame.pack(
            anchor="center", expand=True, fill="both", side="top")
        self.configure(
            height=200,
            style="Heading2.TLabelframe",
            text='Settings',
            width=200)
        # Layout for 'settings_Labelframe' skipped in custom widget template.

    def SettingsMachine_CB(self):
        pass

    def settingsCW_CB(self):
        pass

    def settingsMisc_CB(self):
        pass

    def settingsChannels_CB(self):
        pass

    def settingsBackup_CB(self):
        pass

    def settingsFactoryReset_CB(self):
        pass

    def settingsReboot_CB(self):
        pass

    def settingsClose_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

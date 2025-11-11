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
class settingsBackupUI(ttk.Labelframe):
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

        self.backupSettings_Frame = ttk.Frame(
            self, name="backupsettings_frame")
        self.backupSettings_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        # First object created
        on_first_object_cb(self.backupSettings_Frame)

        self.label14 = ttk.Label(self.backupSettings_Frame, name="label14")
        self.label14.configure(
            anchor="w",
            justify="right",
            style="Heading2b.TLabel",
            text='Setting')
        self.label14.grid(column=0, padx=5, row=0, sticky="w")
        self.label15 = ttk.Label(self.backupSettings_Frame, name="label15")
        self.label15.configure(
            anchor="e",
            justify="center",
            style="Heading2b.TLabel",
            text='Factory\nValue')
        self.label15.grid(column=1, row=0, sticky="ew")
        self.label16 = ttk.Label(self.backupSettings_Frame, name="label16")
        self.label16.configure(
            anchor="e",
            justify="center",
            style="Heading2b.TLabel",
            text='Current\nValue')
        self.label16.grid(column=2, row=0, sticky="ew")
        self.label17 = ttk.Label(self.backupSettings_Frame, name="label17")
        self.label17.configure(
            anchor="e",
            justify="center",
            style="Heading2b.TLabel",
            text='Config\nFile')
        self.label17.grid(column=3, row=0, sticky="ew")
        frame2 = ttk.Frame(self.backupSettings_Frame)
        frame2.configure(height=200, width=200)
        separator1 = ttk.Separator(frame2)
        separator1.configure(orient="horizontal")
        separator1.pack(expand=True, fill="x", side="top")
        frame2.grid(column=0, columnspan=4, row=1, sticky="ew")
        self.Master_Cal_Heading_Label = ttk.Label(
            self.backupSettings_Frame, name="master_cal_heading_label")
        self.Master_Cal_Heading_Label.configure(
            anchor="w", style="Heading2b.TLabel", text='Master Cal:', width=10)
        self.Master_Cal_Heading_Label.grid(column=0, padx=5, pady=5, row=2)
        self.EEPROM_Factory_Master_Cal_Label = ttk.Label(
            self.backupSettings_Frame, name="eeprom_factory_master_cal_label")
        self.EEPROM_Factory_Master_Cal_VAR = tk.StringVar(value='label3')
        self.EEPROM_Factory_Master_Cal_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label3',
            textvariable=self.EEPROM_Factory_Master_Cal_VAR,
            width=10)
        self.EEPROM_Factory_Master_Cal_Label.grid(
            column=1, padx="0 5", pady=5, row=2, sticky="e")
        self.EEPROM_Current_Master_Cal_Label = ttk.Label(
            self.backupSettings_Frame, name="eeprom_current_master_cal_label")
        self.EEPROM_Current_Master_Cal_VAR = tk.StringVar(value='label4')
        self.EEPROM_Current_Master_Cal_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label4',
            textvariable=self.EEPROM_Current_Master_Cal_VAR,
            width=10)
        self.EEPROM_Current_Master_Cal_Label.grid(
            column=2, padx="0 5", pady=5, row=2, sticky="e")
        self.ConfigFile_Master_Cal_Label = ttk.Label(
            self.backupSettings_Frame, name="configfile_master_cal_label")
        self.ConfigFile_Master_Cal_VAR = tk.StringVar(value='label4')
        self.ConfigFile_Master_Cal_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label4',
            textvariable=self.ConfigFile_Master_Cal_VAR,
            width=10)
        self.ConfigFile_Master_Cal_Label.grid(
            column=3, padx="0 5", pady=5, row=2, sticky="e")
        self.SSB_BFO_Heading_Label = ttk.Label(
            self.backupSettings_Frame, name="ssb_bfo_heading_label")
        self.SSB_BFO_Heading_Label.configure(
            anchor="w", style="Heading2b.TLabel", text='SSB BFO:', width=10)
        self.SSB_BFO_Heading_Label.grid(column=0, padx=5, pady="0 5", row=3)
        self.EEPROM_Factory_SSB_BFO_Label = ttk.Label(
            self.backupSettings_Frame, name="eeprom_factory_ssb_bfo_label")
        self.EEPROM_Factory_SSB_BFO_VAR = tk.StringVar(value='label3')
        self.EEPROM_Factory_SSB_BFO_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label3',
            textvariable=self.EEPROM_Factory_SSB_BFO_VAR,
            width=10)
        self.EEPROM_Factory_SSB_BFO_Label.grid(
            column=1, padx="0 5", pady="0 5", row=3, sticky="e")
        self.EEPROM_Current_SSB_BFO_Label = ttk.Label(
            self.backupSettings_Frame, name="eeprom_current_ssb_bfo_label")
        self.EEPROM_Current_SSB_BFO_VAR = tk.StringVar(value='label4')
        self.EEPROM_Current_SSB_BFO_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label4',
            textvariable=self.EEPROM_Current_SSB_BFO_VAR,
            width=10)
        self.EEPROM_Current_SSB_BFO_Label.grid(
            column=2, padx="0 5", pady="0 5", row=3, sticky="e")
        self.ConfigFile_SSB_BFO_Label = ttk.Label(
            self.backupSettings_Frame, name="configfile_ssb_bfo_label")
        self.ConfigFile_SSB_BFO_VAR = tk.StringVar(value='label4')
        self.ConfigFile_SSB_BFO_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label4',
            textvariable=self.ConfigFile_SSB_BFO_VAR,
            width=10)
        self.ConfigFile_SSB_BFO_Label.grid(
            column=3, padx="0 5", pady="0 5", row=3, sticky="e")
        self.CW_BFO_Heading_Label = ttk.Label(
            self.backupSettings_Frame, name="cw_bfo_heading_label")
        self.CW_BFO_Heading_Label.configure(
            anchor="w", style="Heading2b.TLabel", text='CW BFO:', width=10)
        self.CW_BFO_Heading_Label.grid(column=0, padx=5, pady="0 5", row=4)
        self.EEPROM_Factory_CW_BFO_Label = ttk.Label(
            self.backupSettings_Frame, name="eeprom_factory_cw_bfo_label")
        self.EEPROM_Factory_CW_BFO_VAR = tk.StringVar(value='label3')
        self.EEPROM_Factory_CW_BFO_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label3',
            textvariable=self.EEPROM_Factory_CW_BFO_VAR,
            width=10)
        self.EEPROM_Factory_CW_BFO_Label.grid(
            column=1, padx="0 5", pady="0 5", row=4, sticky="e")
        self.EEPROM_Current_CW_BFO_Label = ttk.Label(
            self.backupSettings_Frame, name="eeprom_current_cw_bfo_label")
        self.EEPROM_Current_CW_BFO_VAR = tk.StringVar(value='label4')
        self.EEPROM_Current_CW_BFO_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label4',
            textvariable=self.EEPROM_Current_CW_BFO_VAR,
            width=10)
        self.EEPROM_Current_CW_BFO_Label.grid(
            column=2, padx="0 5", pady="0 5", row=4, sticky="e")
        self.ConfigFIle_CW_BFO_Label = ttk.Label(
            self.backupSettings_Frame, name="configfile_cw_bfo_label")
        self.ConfigFIle_CW_BFO_VAR = tk.StringVar(value='label4')
        self.ConfigFIle_CW_BFO_Label.configure(
            anchor="e",
            justify="right",
            style="Heading3b.TLabel",
            text='label4',
            textvariable=self.ConfigFIle_CW_BFO_VAR,
            width=10)
        self.ConfigFIle_CW_BFO_Label.grid(
            column=3, padx="0 5", pady="0 5", row=4, sticky="e")
        frame3 = ttk.Frame(self.backupSettings_Frame)
        frame3.configure(height=200, width=200)
        separator2 = ttk.Separator(frame3)
        separator2.configure(orient="horizontal")
        separator2.pack(expand=True, fill="x", side="top")
        frame3.grid(column=0, columnspan=4, row=5, sticky="ew")
        self.backupSettings_Frame.grid(column=0, pady="10 0", row=1)
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
        self.closingFrame.grid(column=0, pady=10, row=3)
        self.configure(
            height=400,
            style="Heading2.TLabelframe",
            text='Radio Backup',
            width=600)
        # Layout for 'labelframe1' skipped in custom widget template.

    def apply_CB(self):
        pass

    def cancel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsBackupUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

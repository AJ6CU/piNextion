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
class cwSettingsUI(tk.Toplevel):
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

        labelframe1 = ttk.Labelframe(self)
        labelframe1.configure(
            height=400,
            style="Heading2.TLabelframe",
            text='CW Settings',
            width=600)
        # First object created
        on_first_object_cb(labelframe1)

        frame1 = ttk.Frame(labelframe1)
        frame1.configure(height=200, style="Normal.TFrame", width=200)
        self.General_CW_Settings_Frame = ttk.Frame(
            frame1, name="general_cw_settings_frame")
        self.General_CW_Settings_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.CW_KEY_TYPE_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_key_type_label")
        self.CW_KEY_TYPE_LABEL.configure(
            style="Heading4.TLabel", text='Key Type')
        self.CW_KEY_TYPE_LABEL.grid(column=0, pady="0 10", row=0)
        self.key_type_value_VAR = tk.StringVar(value='STRAIGHT')
        __values = ['STRAIGHT', 'IAMBICA', 'IAMBICB']
        self.CW_KEY_TYPE_WIDGET = tk.OptionMenu(
            self.General_CW_Settings_Frame,
            self.key_type_value_VAR,
            *__values,
            command=None)
        self.CW_KEY_TYPE_WIDGET.grid(column=1, row=0, sticky="w")
        self.CW_SIDETONE_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_sidetone_label")
        self.CW_SIDETONE_LABEL.configure(
            style="Heading4.TLabel", text='Sidetone (HZ)')
        self.CW_SIDETONE_LABEL.grid(column=0, row=2, sticky="w")
        self.CW_SIDETONE_WIDGET = ttk.Entry(
            self.General_CW_Settings_Frame,
            name="cw_sidetone_widget")
        self.tone_value_VAR = tk.StringVar(value='599')
        self.CW_SIDETONE_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.tone_value_VAR,
            validate="focus",
            width=10)
        _text_ = '599'
        self.CW_SIDETONE_WIDGET.delete("0", "end")
        self.CW_SIDETONE_WIDGET.insert("0", _text_)
        self.CW_SIDETONE_WIDGET.grid(column=1, row=2)
        _validatecmd = (
            self.CW_SIDETONE_WIDGET.register(
                self.validate_CW_SIDETONE), "%P", "%V")
        self.CW_SIDETONE_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_SPEED_WPM_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_speed_wpm_label")
        self.CW_SPEED_WPM_LABEL.configure(
            style="Heading4.TLabel", text='Speed (WPM)')
        self.CW_SPEED_WPM_LABEL.grid(column=0, row=6, sticky="w")
        self.CW_SPEED_WPM_WIDGET = ttk.Entry(
            self.General_CW_Settings_Frame,
            name="cw_speed_wpm_widget")
        self.key_speed_value_VAR = tk.StringVar()
        self.CW_SPEED_WPM_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.key_speed_value_VAR,
            validate="focus",
            width=10)
        self.CW_SPEED_WPM_WIDGET.grid(column=1, row=6)
        _validatecmd = (
            self.CW_SPEED_WPM_WIDGET.register(
                self.validate_CW_SPEED_WPM), "%P", "%V")
        self.CW_SPEED_WPM_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_START_MS_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_start_ms_label")
        self.CW_START_MS_LABEL.configure(
            style="Heading4.TLabel",
            text='Delay Starting TX (ms)')
        self.CW_START_MS_LABEL.grid(column=0, row=10, sticky="w")
        self.CW_START_MS_WIDGET = ttk.Entry(
            self.General_CW_Settings_Frame,
            name="cw_start_ms_widget")
        self.delay_starting_tx_value_VAR = tk.StringVar()
        self.CW_START_MS_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.delay_starting_tx_value_VAR,
            validate="focus",
            width=10)
        self.CW_START_MS_WIDGET.grid(column=1, row=10)
        _validatecmd = (
            self.CW_START_MS_WIDGET.register(
                self.validate_CW_START_MS), "%P", "%V")
        self.CW_START_MS_WIDGET.configure(validatecommand=_validatecmd)
        self.CW_DELAY_MS_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_delay_ms_label")
        self.CW_DELAY_MS_LABEL.configure(
            style="Heading4.TLabel",
            text='Delay Returning to RX (ms)')
        self.CW_DELAY_MS_LABEL.grid(column=0, row=14, sticky="w")
        self.CW_DELAY_MS_WIDGET = ttk.Entry(
            self.General_CW_Settings_Frame,
            name="cw_delay_ms_widget")
        self.delay_returning_to_rx_value_VAR = tk.StringVar()
        self.CW_DELAY_MS_WIDGET.configure(
            justify="right",
            style="Normal.TEntry",
            textvariable=self.delay_returning_to_rx_value_VAR,
            validate="focus",
            width=10)
        self.CW_DELAY_MS_WIDGET.grid(column=1, row=14)
        _validatecmd = (
            self.CW_DELAY_MS_WIDGET.register(
                self.validate_CW_DELAY_MS), "%P", "%V")
        self.CW_DELAY_MS_WIDGET.configure(validatecommand=_validatecmd)
        self.label209 = ttk.Label(
            self.General_CW_Settings_Frame,
            name="label209")
        self.label209.configure(
            style="Heading4.TLabel",
            text='VFO Freq displays')
        self.label209.grid(column=0, pady="0 10", row=15)
        self.CW_DISPLAY_FREQ = tk.StringVar(value='TX')
        __values = ['TX', 'RX']
        self.CW_DISPLAY_FREQ_WIDGET = tk.OptionMenu(
            self.General_CW_Settings_Frame, self.CW_DISPLAY_FREQ, *__values, command=None)
        self.CW_DISPLAY_FREQ_WIDGET.grid(column=1, pady=10, row=15)
        self.text4 = tk.Text(self.General_CW_Settings_Frame, name="text4")
        self.text4.configure(
            background="#eeeeee",
            borderwidth=2,
            font="TkMenuFont",
            foreground="black",
            height=4,
            padx=5,
            pady=5,
            relief="groove",
            state="disabled",
            takefocus=False,
            width=57,
            wrap="word")
        _text_ = 'When in CW mode, your VFO can display either your TX or RX frequency. TX seems to be generally the preferred choice. For more details, see:\nhttp://www.hamskey.com/2018/07/cw-frequency-in-ubitx.html\n'
        self.text4.configure(state="normal")
        self.text4.insert("0.0", _text_)
        self.text4.configure(state="disabled")
        self.text4.grid(column=2, padx="10 0", row=15)
        self.General_CW_Settings_Frame.pack(padx="50 0", side="top")
        frame1.pack(side="top")
        self.closingFrame = ttk.Frame(labelframe1, name="closingframe")
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
            pady=10,
            side="top")
        labelframe1.pack(expand=True, fill="both", side="top")
        self.configure(height=400, width=600)
        # Layout for 'cw_settings_window' skipped in custom widget template.

    def validate_CW_SIDETONE(self, p_entry_value, v_condition):
        pass

    def validate_CW_SPEED_WPM(self, p_entry_value, v_condition):
        pass

    def validate_CW_START_MS(self, p_entry_value, v_condition):
        pass

    def validate_CW_DELAY_MS(self, p_entry_value, v_condition):
        pass

    def apply_CB(self):
        pass

    def cancel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = cwSettingsUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

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
class cwSettingsUI(ttk.Labelframe):
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

        self.General_CW_Settings_Frame = ttk.Frame(
            frame1, name="general_cw_settings_frame")
        self.General_CW_Settings_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.CW_KEY_TYPE_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_key_type_label")
        self.CW_KEY_TYPE_LABEL.configure(
            style="Heading1b.TLabel", text='Key Type')
        self.CW_KEY_TYPE_LABEL.grid(column=0, pady="40 0", row=0, sticky="e")
        self.CW_Keytype_Widget_Combobox = Combobox(
            self.General_CW_Settings_Frame,
            name="cw_keytype_widget_combobox")
        self.key_type_value_VAR = tk.StringVar()
        self.CW_Keytype_Widget_Combobox.configure(
            justify="center",
            keyvariable=self.key_type_value_VAR,
            style="ComboBox1.TCombobox",
            values='STRAIGHT IAMBICA IAMBICB',
            width=10)
        self.CW_Keytype_Widget_Combobox.grid(
            column=1, padx="20 0", pady="40 0", row=0, sticky="w")
        self.CW_SIDETONE_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_sidetone_label")
        self.CW_SIDETONE_LABEL.configure(
            style="Heading1b.TLabel", text='Sidetone (HZ)')
        self.CW_SIDETONE_LABEL.grid(column=0, pady="40 0", row=2, sticky="e")
        self.CW_Sidetone_Widget_Combobox = Combobox(
            self.General_CW_Settings_Frame,
            name="cw_sidetone_widget_combobox")
        self.tone_value_VAR = tk.StringVar()
        self.CW_Sidetone_Widget_Combobox.configure(
            justify="center",
            keyvariable=self.tone_value_VAR,
            style="ComboBox1.TCombobox",
            width=4)
        self.CW_Sidetone_Widget_Combobox.grid(
            column=1, padx="20 0", pady="40 0", row=2, sticky="w")
        self.CW_SPEED_WPM_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_speed_wpm_label")
        self.CW_SPEED_WPM_LABEL.configure(
            style="Heading1b.TLabel", text='Speed (WPM)')
        self.CW_SPEED_WPM_LABEL.grid(column=0, pady="40 0", row=6, sticky="e")
        self.CW_Speed_WPM_Widget_Combobox = Combobox(
            self.General_CW_Settings_Frame,
            name="cw_speed_wpm_widget_combobox")
        self.key_speed_value_VAR = tk.StringVar()
        self.CW_Speed_WPM_Widget_Combobox.configure(
            justify="center",
            keyvariable=self.key_speed_value_VAR,
            style="ComboBox1.TCombobox",
            width=4)
        self.CW_Speed_WPM_Widget_Combobox.grid(
            column=1, padx="20 0", pady="40 0", row=6, sticky="w")
        self.CW_START_MS_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_start_ms_label")
        self.CW_START_MS_LABEL.configure(
            style="Heading1b.TLabel",
            text='Delay Starting TX (ms)')
        self.CW_START_MS_LABEL.grid(column=3, pady="40 0", row=0, sticky="e")
        self.CW_Start_MS_Widget_Combobox = Combobox(
            self.General_CW_Settings_Frame,
            name="cw_start_ms_widget_combobox")
        self.delay_starting_tx_value_VAR = tk.StringVar()
        self.CW_Start_MS_Widget_Combobox.configure(
            justify="center",
            keyvariable=self.delay_starting_tx_value_VAR,
            style="ComboBox1.TCombobox",
            width=4)
        self.CW_Start_MS_Widget_Combobox.grid(
            column=4, padx=20, pady="40 0", row=0, sticky="w")
        self.CW_DELAY_MS_LABEL = ttk.Label(
            self.General_CW_Settings_Frame,
            name="cw_delay_ms_label")
        self.CW_DELAY_MS_LABEL.configure(
            style="Heading1b.TLabel",
            text='Delay Returning to RX (ms)')
        self.CW_DELAY_MS_LABEL.grid(column=3, pady="40 0", row=2, sticky="e")
        self.CW_Delay_MS_Widget_Combobox = Combobox(
            self.General_CW_Settings_Frame,
            name="cw_delay_ms_widget_combobox")
        self.delay_returning_to_rx_value_VAR = tk.StringVar()
        self.CW_Delay_MS_Widget_Combobox.configure(
            justify="center",
            keyvariable=self.delay_returning_to_rx_value_VAR,
            style="ComboBox1.TCombobox",
            width=4)
        self.CW_Delay_MS_Widget_Combobox.grid(
            column=4, padx=20, pady="40 0", row=2, sticky="w")
        self.label209 = ttk.Label(
            self.General_CW_Settings_Frame,
            name="label209")
        self.label209.configure(
            style="Heading1b.TLabel",
            text='VFO Freq Displays')
        self.label209.grid(column=3, pady="40 0", row=6, sticky="e")
        self.CW_Display_Freq_Combobox = Combobox(
            self.General_CW_Settings_Frame,
            name="cw_display_freq_combobox")
        self.CW_Display_TXFreq_VAR = tk.StringVar()
        self.CW_Display_Freq_Combobox.configure(
            justify="center",
            keyvariable=self.CW_Display_TXFreq_VAR,
            style="ComboBox1.TCombobox",
            values='TX RX',
            width=4)
        self.CW_Display_Freq_Combobox.grid(
            column=4, padx="20 0", pady="40 0", row=6, sticky="w")
        self.text4 = tk.Text(self.General_CW_Settings_Frame, name="text4")
        self.text4.configure(
            background="#eeeeee",
            borderwidth=2,
            font="TkMenuFont",
            foreground="black",
            height=6,
            padx=5,
            pady=5,
            relief="groove",
            state="disabled",
            takefocus=False,
            width=30,
            wrap="word")
        _text_ = 'Controls whether the VFO will display the TX or RX frequency while in CW.\n\nThis setting will be reset to that stored in the EEPROM on reboot.  Use the Settings Editor to make a permanent change.'
        self.text4.configure(state="normal")
        self.text4.insert("0.0", _text_)
        self.text4.configure(state="disabled")
        self.text4.grid(column=2, columnspan=5, padx="70 0", pady=20, row=15)
        self.General_CW_Settings_Frame.pack(padx="50 0", side="top")
        frame1.pack(side="top")
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
            pady=10,
            side="top")
        self.configure(
            height=400,
            style="Heading2.TLabelframe",
            text='CW Settings',
            width=600)
        # Layout for 'labelframe1' skipped in custom widget template.

    def apply_CB(self):
        pass

    def cancel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = cwSettingsUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

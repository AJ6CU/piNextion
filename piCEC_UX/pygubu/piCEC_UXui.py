#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from JogwheelCustom import JogwheelCustom


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
class piCECNextionUI(ttk.Frame):
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

        self.menuBar_Frame = ttk.Frame(self, name="menubar_frame")
        self.menuBar_Frame.configure(
            borderwidth=5,
            height=50,
            style="Normal.TFrame",
            width=800)
        # First object created
        on_first_object_cb(self.menuBar_Frame)

        self.settings_Button = ttk.Button(
            self.menuBar_Frame, name="settings_button")
        self.settings_VAR = tk.StringVar(value='  \nSETTINGS\n  ')
        self.settings_Button.configure(
            style="Button2b.TButton",
            text='  \nSETTINGS\n  ',
            textvariable=self.settings_VAR,
            width=12)
        self.settings_Button.grid(column=0, padx="0 2", row=0, sticky="ns")
        self.settings_Button.configure(command=self.settings_CB)
        self.vfo_Button = ttk.Button(self.menuBar_Frame, name="vfo_button")
        self.vfo_VAR = tk.StringVar(value='\nVFO\n')
        self.vfo_Button.configure(
            state="normal",
            style="Button2b.TButton",
            text='\nVFO\n',
            textvariable=self.vfo_VAR,
            width=12)
        self.vfo_Button.grid(column=1, padx="0 2", row=0, sticky="ns")
        self.vfo_Button.configure(command=self.vfo_CB)
        self.mode_select_Menubutton = ttk.Menubutton(
            self.menuBar_Frame, name="mode_select_menubutton")
        self.primary_Mode_VAR = tk.StringVar(value=' \nMode\n')
        self.mode_select_Menubutton.configure(
            style="Heading2b.TMenubutton",
            text=' \nMode\n',
            textvariable=self.primary_Mode_VAR,
            width=9)
        self.menu1 = tk.Menu(self.mode_select_Menubutton)
        self.menu1.configure(tearoff=False)
        self.menu1.add(
            "command",
            command=self.mode_lsb_CB,
            font="{Arial} 36 {}",
            label='LSB',
            state="normal")
        self.menu1.add(
            "command",
            command=self.mode_usb_CB,
            font="{Arial} 36 {}",
            label='USB')
        self.menu1.add(
            "command",
            command=self.mode_cwl_CB,
            font="{Arial} 36 {}",
            label='CWL')
        self.menu1.add(
            "command",
            command=self.mode_cwu_CB,
            font="{Arial} 36 {}",
            label='CWU')
        self.mode_select_Menubutton.configure(menu=self.menu1)
        self.mode_select_Menubutton.grid(
            column=2, padx="0 2", row=0, sticky="ns")
        self.band_up_Button = ttk.Button(
            self.menuBar_Frame, name="band_up_button")
        self.band_up_VAR = tk.StringVar(value='\nBAND UP\n')
        self.band_up_Button.configure(
            style="Button2b.TButton",
            text='\nBAND UP\n',
            textvariable=self.band_up_VAR,
            width=12)
        self.band_up_Button.grid(column=3, padx="0 2", row=0, sticky="ns")
        self.band_up_Button.configure(command=self.band_up_CB)
        self.band_down_Button = ttk.Button(
            self.menuBar_Frame, name="band_down_button")
        self.band_down_VAR = tk.StringVar(value='\nBAND DN\n')
        self.band_down_Button.configure(
            style="Button2b.TButton",
            text='\nBAND DN\n',
            textvariable=self.band_down_VAR,
            width=12)
        self.band_down_Button.grid(column=4, padx="0 2", row=0, sticky="ns")
        self.band_down_Button.configure(command=self.band_down_CB)
        self.lock_Button = ttk.Button(self.menuBar_Frame, name="lock_button")
        self.lock_VAR = tk.StringVar(value='\nLOCK\n')
        self.lock_Button.configure(
            style="Button2b.TButton",
            text='\nLOCK\n',
            textvariable=self.lock_VAR,
            width=12)
        self.lock_Button.grid(column=5, padx="0 2", row=0, sticky="ns")
        self.lock_Button.configure(command=self.lock_CB)
        self.speaker_Button = ttk.Button(
            self.menuBar_Frame, name="speaker_button")
        self.speaker_VAR = tk.StringVar(value='\nSPEAKER\n')
        self.speaker_Button.configure(
            style="Button2b.TButton",
            text='\nSPEAKER\n',
            textvariable=self.speaker_VAR,
            width=12)
        self.speaker_Button.grid(column=6, row=0, sticky="ns")
        self.speaker_Button.configure(command=self.speaker_CB)
        self.menuBar_Frame.pack(anchor="n", expand=True, fill="x", side="top")
        self.frame2 = ttk.Frame(self)
        self.frame2.configure(height=200, style="Normal.TFrame", width=200)
        self.vfoA_Frame = ttk.Frame(self.frame2, name="vfoa_frame")
        self.vfoA_Frame.configure(
            borderwidth=3,
            style="NormalOutline.TFrame",
            width=480)
        self.rxTX_Status_Frame = ttk.Frame(
            self.vfoA_Frame, name="rxtx_status_frame")
        self.rxTX_Status_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.rx_Status_Light_Label = ttk.Label(
            self.rxTX_Status_Frame, name="rx_status_light_label")
        self.rx_Status_Light_Label.configure(
            borderwidth=4,
            state="normal",
            style="GreenLED.TLabel",
            text='  RX',
            width=5)
        self.rx_Status_Light_Label.grid(column=0, pady=10, row=0)
        self.tx_Status_Light_Label = ttk.Label(
            self.rxTX_Status_Frame, name="tx_status_light_label")
        self.tx_Status_Light_Label.configure(
            borderwidth=4,
            state="disabled",
            style="RedLED.TLabel",
            text='  TX',
            width=5)
        self.tx_Status_Light_Label.grid(column=0, pady=15, row=1)
        self.stop_Button = ttk.Button(
            self.rxTX_Status_Frame, name="stop_button")
        self.stop_Button.configure(
            state="normal",
            style="RedButton2.TButton",
            text='\nSTOP!\n',
            width=6)
        self.stop_Button.grid(column=1, padx="20 10", row=0, rowspan=2)
        self.stop_Button.configure(command=self.stop_CB)
        self.separator2 = ttk.Separator(self.rxTX_Status_Frame)
        self.separator2.configure(orient="vertical")
        self.separator2.grid(column=2, row=0, rowspan=3, sticky="ns")
        self.rxTX_Status_Frame.grid(column=0, padx=15, row=0, sticky="e")
        self.vfo_display_Frame = ttk.Frame(
            self.vfoA_Frame, name="vfo_display_frame")
        self.vfo_display_Frame.configure(style="Normal.TFrame", width=200)
        self.primary_VFO_Label = ttk.Label(
            self.vfo_display_Frame, name="primary_vfo_label")
        self.primary_VFO_VAR = tk.StringVar(value='99999999')
        self.primary_VFO_Label.configure(
            anchor="e",
            style="VFO.TLabel",
            text='99999999',
            textvariable=self.primary_VFO_VAR,
            width=8)
        self.primary_VFO_Label.pack(anchor="e", side="top")
        self.frame1 = ttk.Frame(self.vfo_display_Frame)
        self.frame1.configure(height=10, style="Normal.TFrame", width=200)
        self.digit7_Highlight_Label = ttk.Label(
            self.frame1, name="digit7_highlight_label")
        self.digit7_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit7_Highlight_Label.pack(padx="7 0", side="left")
        self.digit6_Highlight_Label = ttk.Label(
            self.frame1, name="digit6_highlight_label")
        self.digit6_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit6_Highlight_Label.pack(padx="19 0", side="left")
        self.digit5_Highlight_Label = ttk.Label(
            self.frame1, name="digit5_highlight_label")
        self.digit5_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit5_Highlight_Label.pack(padx="19 0", side="left")
        self.digit4_Highlight_Label = ttk.Label(
            self.frame1, name="digit4_highlight_label")
        self.digit4_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit4_Highlight_Label.pack(padx="19 0", side="left")
        self.digit3_Highlight_Label = ttk.Label(
            self.frame1, name="digit3_highlight_label")
        self.digit3_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit3_Highlight_Label.pack(padx="19 0", side="left")
        self.digit2_Highlight_Label = ttk.Label(
            self.frame1, name="digit2_highlight_label")
        self.digit2_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit2_Highlight_Label.pack(padx="19 0", side="left")
        self.digit1_Highlight_Label = ttk.Label(
            self.frame1, name="digit1_highlight_label")
        self.digit1_Highlight_Label.configure(style="OffLED.TLabel", width=10)
        self.digit1_Highlight_Label.pack(anchor="w", padx="19 0", side="left")
        self.frame1.pack(anchor="w", padx=0, side="bottom")
        self.vfo_display_Frame.grid(column=1, padx="48 0", row=0, sticky="e")
        self.vfoA_Frame.grid(column=0, row=0, sticky="w")
        self.vfoB_Frame = ttk.Frame(self.frame2, name="vfob_frame")
        self.vfoB_Frame.configure(borderwidth=3, style="NormalOutline.TFrame")
        self.vfo_Frame = ttk.Frame(self.vfoB_Frame, name="vfo_frame")
        self.vfo_Frame.configure(style="Normal.TFrame")
        self.secondary_VFO_Label = ttk.Label(
            self.vfo_Frame, name="secondary_vfo_label")
        self.secondary_VFO_VAR = tk.StringVar(value='99999999')
        self.secondary_VFO_Label.configure(
            style="Heading1.TLabel",
            text='99999999',
            textvariable=self.secondary_VFO_VAR)
        self.secondary_VFO_Label.pack(anchor="nw", side="left")
        self.secondary_Mode_Label = ttk.Label(
            self.vfo_Frame, name="secondary_mode_label")
        self.secondary_Mode_VAR = tk.StringVar(value='CWL')
        self.secondary_Mode_Label.configure(
            style="Heading1.TLabel",
            text='CWL',
            textvariable=self.secondary_Mode_VAR)
        self.secondary_Mode_Label.pack(anchor="ne", padx="5 0", side="right")
        self.vfo_Frame.pack(padx="20 0", side="left")
        self.callsign_Frame = ttk.Frame(self.vfoB_Frame, name="callsign_frame")
        self.callsign_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.label5 = ttk.Label(self.callsign_Frame)
        self.label5.configure(
            style="Heading4b.TLabel",
            text='AJ6CUxyz',
            width=10)
        self.label5.pack(anchor="nw", padx="0 10", side="left")
        self.label6 = ttk.Label(self.callsign_Frame)
        self.label6.configure(style="Heading4b.TLabel", text='V2.0 RCLxyz')
        self.label6.pack(anchor="nw", side="left")
        self.callsign_Frame.pack(
            expand=False,
            fill="y",
            padx="70 0",
            pady=10,
            side="left")
        self.tuning_Step_Frame = ttk.Frame(
            self.vfoB_Frame, name="tuning_step_frame")
        self.tuning_Step_Frame.configure(style="Normal.TFrame", width=200)
        self.tuning_Preset_Button = ttk.Button(
            self.tuning_Step_Frame, name="tuning_preset_button")
        self.tuning_Preset_Label_VAR = tk.StringVar(value='0')
        self.tuning_Preset_Button.configure(
            style="Button2b.TButton",
            text='0',
            textvariable=self.tuning_Preset_Label_VAR,
            width=10)
        self.tuning_Preset_Button.pack(padx="12 0", side="left")
        self.tuning_Preset_Button.configure(
            command=self.tuning_Preset_Select_CB)
        self.tuning_Preset_Units_Label = ttk.Label(
            self.tuning_Step_Frame, name="tuning_preset_units_label")
        self.tuning_Preset_Units_Label.configure(
            style="Heading1.TLabel", text='Hz')
        self.tuning_Preset_Units_Label.pack(padx=15, side="left")
        self.tuning_Step_Frame.pack(padx="75 0", pady="5 0", side="right")
        self.vfoB_Frame.grid(column=0, row=1, sticky="w")
        self.control_Meter_Tuning_Frame = ttk.Frame(
            self.frame2, name="control_meter_tuning_frame")
        self.control_Meter_Tuning_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.secondary_menu_Frame = ttk.Frame(
            self.control_Meter_Tuning_Frame,
            name="secondary_menu_frame")
        self.secondary_menu_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.signal_Control_Frame = ttk.Frame(
            self.secondary_menu_Frame, name="signal_control_frame")
        self.signal_Control_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.split_Button = ttk.Button(
            self.signal_Control_Frame, name="split_button")
        self.split_Button.configure(style="Button2b.TButton", text='\nSPLIT\n')
        self.split_Button.pack(anchor="nw", padx=20, side="left")
        self.split_Button.configure(command=self.split_CB)
        self.rit_Button = ttk.Button(
            self.signal_Control_Frame, name="rit_button")
        self.rit_Button.configure(style="Button2b.TButton", text='\nRIT\n')
        self.rit_Button.pack(anchor="nw", padx="0 20", side="left")
        self.rit_Button.configure(command=self.rit_CB)
        self.store_Button = ttk.Button(
            self.signal_Control_Frame, name="store_button")
        self.store_Button.configure(style="Button2b.TButton", text='\nSTORE\n')
        self.store_Button.pack(anchor="nw", padx="0 20", side="left")
        self.store_Button.configure(command=self.store_CB)
        self.recall_Button = ttk.Button(
            self.signal_Control_Frame, name="recall_button")
        self.recall_Button.configure(
            style="Button2b.TButton", text='\nRECALL\n')
        self.recall_Button.pack(anchor="nw", side="left")
        self.recall_Button.configure(command=self.recall_CB)
        self.signal_Control_Frame.grid(column=0, pady=10, row=0, sticky="n")
        self.secondary_menu_Frame.grid(column=0, row=0)
        self.tuning_Preset_Selection_Frame = ttk.Frame(
            self.control_Meter_Tuning_Frame,
            name="tuning_preset_selection_frame")
        self.tuning_Preset_Selection_Frame.configure(
            height=200, style="Normal.TFrame", width=50)
        self.tuning_Preset_5_Radiobutton = ttk.Radiobutton(
            self.tuning_Preset_Selection_Frame, name="tuning_preset_5_radiobutton")
        self.tuning_Preset_5_VAR = tk.StringVar(value='50000')
        self.tuning_Preset_Selection_VAR = tk.StringVar(value='5')
        self.tuning_Preset_5_Radiobutton.configure(
            style="RadioButton3.TRadiobutton",
            text='50000',
            textvariable=self.tuning_Preset_5_VAR,
            value=5,
            variable=self.tuning_Preset_Selection_VAR,
            width=11)
        self.tuning_Preset_5_Radiobutton.pack(side="top")
        self.tuning_Preset_5_Radiobutton.configure(
            command=self.tuning_Preset_5_CB)
        self.tuning_Preset_4_Radiobutton = ttk.Radiobutton(
            self.tuning_Preset_Selection_Frame, name="tuning_preset_4_radiobutton")
        self.tuning_Preset_4_VAR = tk.StringVar(value='10000')
        self.tuning_Preset_4_Radiobutton.configure(
            style="RadioButton3.TRadiobutton",
            text='10000',
            textvariable=self.tuning_Preset_4_VAR,
            value=4,
            variable=self.tuning_Preset_Selection_VAR,
            width=11)
        self.tuning_Preset_4_Radiobutton.pack(side="top")
        self.tuning_Preset_4_Radiobutton.configure(
            command=self.tuning_Preset_4_CB)
        self.tuning_Preset_3_Radiobutton = ttk.Radiobutton(
            self.tuning_Preset_Selection_Frame, name="tuning_preset_3_radiobutton")
        self.tuning_Preset_3_VAR = tk.StringVar(value='5000')
        self.tuning_Preset_3_Radiobutton.configure(
            style="RadioButton3.TRadiobutton",
            text='5000',
            textvariable=self.tuning_Preset_3_VAR,
            value=3,
            variable=self.tuning_Preset_Selection_VAR,
            width=11)
        self.tuning_Preset_3_Radiobutton.pack(side="top")
        self.tuning_Preset_3_Radiobutton.configure(
            command=self.tuning_Preset_3_CB)
        self.tuning_Preset_2_Radiobutton = ttk.Radiobutton(
            self.tuning_Preset_Selection_Frame, name="tuning_preset_2_radiobutton")
        self.tuning_Preset_2_VAR = tk.StringVar(value='1000')
        self.tuning_Preset_2_Radiobutton.configure(
            style="RadioButton3.TRadiobutton",
            text='1000',
            textvariable=self.tuning_Preset_2_VAR,
            value=2,
            variable=self.tuning_Preset_Selection_VAR,
            width=11)
        self.tuning_Preset_2_Radiobutton.pack(side="top")
        self.tuning_Preset_2_Radiobutton.configure(
            command=self.tuning_Preset_2_CB)
        self.tuning_Preset_1_Radiobutton = ttk.Radiobutton(
            self.tuning_Preset_Selection_Frame, name="tuning_preset_1_radiobutton")
        self.tuning_Preset_1_VAR = tk.StringVar(value='100')
        self.tuning_Preset_1_Radiobutton.configure(
            style="RadioButton3.TRadiobutton",
            text='100',
            textvariable=self.tuning_Preset_1_VAR,
            value=1,
            variable=self.tuning_Preset_Selection_VAR,
            width=11)
        self.tuning_Preset_1_Radiobutton.pack(side="top")
        self.tuning_Preset_1_Radiobutton.configure(
            command=self.tuning_Preset_1_CB)
        self.tuning_Preset_Selection_Frame.grid(
            column=1, padx="24 0", pady=5, row=0, rowspan=3, sticky="nw")
        self.sMeter_Frame = ttk.Frame(
            self.control_Meter_Tuning_Frame,
            name="smeter_frame")
        self.sMeter_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.s_meter_Label = ttk.Label(self.sMeter_Frame, name="s_meter_label")
        self.s_meter_Label.configure(style="Heading2b.TLabel", text='S Meter')
        self.s_meter_Label.grid(column=0, row=1, sticky="w")
        self.s_meter_Progressbar = ttk.Progressbar(
            self.sMeter_Frame, name="s_meter_progressbar")
        self.s_meter_Progressbar.configure(
            length=380, maximum=10, orient="horizontal")
        self.s_meter_Progressbar.grid(column=1, row=1, sticky="w")
        self.power_meter_Label = ttk.Label(
            self.sMeter_Frame, name="power_meter_label")
        self.power_meter_Label.configure(
            style="Heading2b.TLabel", text='Power')
        self.power_meter_Label.grid(column=0, row=2, sticky="w")
        self.power_meter_Progressbar = ttk.Progressbar(
            self.sMeter_Frame, name="power_meter_progressbar")
        self.power_meter_Progressbar.configure(
            length=380, maximum=10, orient="horizontal")
        self.power_meter_Progressbar.grid(column=1, row=2)
        self.label7 = ttk.Label(self.sMeter_Frame)
        self.label7.configure(
            style="Heading2b.TLabel",
            text='...................5................7..............8..........9........')
        self.label7.grid(column=1, row=0, sticky="ew")
        self.sMeter_Frame.grid(column=0, row=1)
        self.control_Meter_Tuning_Frame.grid(column=0, row=2, sticky="w")
        self.frame3 = ttk.Frame(self.frame2)
        self.frame3.configure(height=200, style="Normal.TFrame", width=200)
        self.tuning_Jogwheel = JogwheelCustom(
            self.frame3,
            start=0,
            end=9,
            divisions=10,
            button_radius=25,
            value=0,
            progress=False,
            scroll=True,
            scroll_steps=1,
            name="tuning_jogwheel")
        self.tuning_Jogwheel.configure(state="normal")
        self.tuning_Jogwheel.pack(side="top")
        self.tuning_Jogwheel.configure(command=self.tuning_Jogwheel_CB)
        self.tuning_Multiplier_Button = ttk.Button(
            self.frame3, name="tuning_multiplier_button")
        self.tuning_Multiplier_VAR = tk.StringVar(
            value='Tuning Factor\nx 100mhz')
        self.tuning_Multiplier_Button.configure(
            style="Button2b.TButton",
            text='Tuning Factor\nx 100mhz',
            textvariable=self.tuning_Multiplier_VAR)
        self.tuning_Multiplier_Button.pack(anchor="n", pady=5, side="top")
        self.tuning_Multiplier_Button.configure(
            command=self.tuning_Multiplier_Button_CB)
        self.frame3.grid(
            column=1,
            padx="20 0",
            pady=2,
            row=0,
            rowspan=3,
            sticky="n")
        self.frame2.pack(anchor="n", side="top")
        self.ATT_IFS_Adjust_Frame = ttk.Frame(
            self, name="att_ifs_adjust_frame")
        self.ATT_IFS_Adjust_Frame.configure(
            height=50, style="Normal.TFrame", width=800)
        self.att_ifs_Frame = ttk.Frame(
            self.ATT_IFS_Adjust_Frame,
            name="att_ifs_frame")
        self.att_ifs_Frame.configure(
            height=200, style="Normal.TFrame", width=400)
        self.ATT_Frame = ttk.Frame(self.att_ifs_Frame, name="att_frame")
        self.ATT_Frame.configure(height=200, style="Normal.TFrame", width=200)
        self.ATT_Jogwheel = JogwheelCustom(
            self.ATT_Frame,
            start=0,
            end=255,
            divisions=10,
            radius=200,
            button_radius=25,
            value=70,
            scroll_steps=10,
            name="att_jogwheel")
        self.ATT_Jogwheel.configure(state="disabled")
        self.ATT_Jogwheel.pack(anchor="center", padx=30, side="top")
        self.ATT_Jogwheel.configure(command=self.updateATTValue_CB)
        self.ATT_Jogwheel.bind(
            "<ButtonPress>",
            self.ATT_Jogwheel_ButtonPressed_CB,
            add="+")
        self.ATT_Jogwheel.bind(
            "<ButtonRelease>",
            self.ATT_Jogwheel_ButtonReleased_CB,
            add="+")
        self.ATT_Status_Label = ttk.Label(
            self.ATT_Frame, name="att_status_label")
        self.ATT_Status_VAR = tk.StringVar(value='ATT (OFF)')
        self.ATT_Status_Label.configure(
            style="Heading2b.TLabel",
            text='ATT (OFF)',
            textvariable=self.ATT_Status_VAR)
        self.ATT_Status_Label.pack(anchor="center", side="bottom")
        self.ATT_Frame.pack(padx=30, side="left")
        self.IFS_Frame = ttk.Frame(self.att_ifs_Frame, name="ifs_frame")
        self.IFS_Frame.configure(height=200, style="Normal.TFrame", width=200)
        self.IFS_Jogwheel = JogwheelCustom(
            self.IFS_Frame,
            start=-2000,
            end=2000,
            divisions=150,
            radius=200,
            button_radius=25,
            value=0,
            scroll_steps=150,
            name="ifs_jogwheel")
        self.IFS_Jogwheel.configure(state="disabled")
        self.IFS_Jogwheel.pack(anchor="center", padx=30, side="top")
        self.IFS_Jogwheel.configure(command=self.updateIFSValue_CB)
        self.IFS_Jogwheel.bind(
            "<ButtonPress>",
            self.IFS_Jogwheel_ButtonPressed_CB,
            add="+")
        self.IFS_Jogwheel.bind(
            "<ButtonRelease>",
            self.IFS_Jogwheel_ButtonReleased_CB,
            add="+")
        self.IFS_Status_Label = ttk.Label(
            self.IFS_Frame, name="ifs_status_label")
        self.IFS_Status_VAR = tk.StringVar(value='IFS (OFF)')
        self.IFS_Status_Label.configure(
            style="Heading2b.TLabel",
            text='IFS (OFF)',
            textvariable=self.IFS_Status_VAR)
        self.IFS_Status_Label.pack(anchor="center", side="bottom")
        self.IFS_Frame.pack(padx=30, side="left")
        self.att_ifs_Frame.pack(
            anchor="nw",
            expand=False,
            fill="x",
            padx=10,
            side="left")
        self.cw_Info_Frame = ttk.Frame(
            self.ATT_IFS_Adjust_Frame,
            name="cw_info_frame")
        self.cw_Info_Frame.configure(
            borderwidth=5,
            height=200,
            style="NormalOutline.TFrame",
            width=200)
        self.cw_settings_title_Label = ttk.Label(
            self.cw_Info_Frame, name="cw_settings_title_label")
        self.cw_settings_title_Label.configure(
            style="Heading2b.TLabel", text='CW Settings')
        self.cw_settings_title_Label.grid(column=0, columnspan=3, row=0)
        self.tone_Label = ttk.Label(self.cw_Info_Frame, name="tone_label")
        self.tone_Label.configure(style="Heading3b.TLabel", text='Tone')
        self.tone_Label.grid(column=0, row=1, sticky="w")
        self.tone_value_Label = ttk.Label(
            self.cw_Info_Frame, name="tone_value_label")
        self.tone_value_VAR = tk.StringVar(value='799')
        self.tone_value_Label.configure(
            style="Heading3b.TLabel",
            text='799',
            textvariable=self.tone_value_VAR)
        self.tone_value_Label.grid(column=1, padx="0 2", row=1, sticky="w")
        self.tone_units_Label = ttk.Label(
            self.cw_Info_Frame, name="tone_units_label")
        self.tone_units_Label.configure(style="Heading3b.TLabel", text='Hz')
        self.tone_units_Label.grid(column=2, row=1, sticky="w")
        self.key_type_Label = ttk.Label(
            self.cw_Info_Frame, name="key_type_label")
        self.key_type_Label.configure(style="Heading3b.TLabel", text='Key')
        self.key_type_Label.grid(column=0, row=2, sticky="w")
        self.key_type_value_Label = ttk.Label(
            self.cw_Info_Frame, name="key_type_value_label")
        self.key_type_value_VAR = tk.StringVar(value='Straight')
        self.key_type_value_Label.configure(
            style="Heading3b.TLabel",
            text='Straight',
            textvariable=self.key_type_value_VAR)
        self.key_type_value_Label.grid(column=1, row=2, sticky="w")
        self.key_speed_label = ttk.Label(
            self.cw_Info_Frame, name="key_speed_label")
        self.key_speed_label.configure(style="Heading3b.TLabel", text='Speed')
        self.key_speed_label.grid(column=0, row=3, sticky="w")
        self.key_speed_value_Label = ttk.Label(
            self.cw_Info_Frame, name="key_speed_value_label")
        self.key_speed_value_VAR = tk.StringVar(value='1')
        self.key_speed_value_Label.configure(
            style="Heading3b.TLabel",
            text='1',
            textvariable=self.key_speed_value_VAR)
        self.key_speed_value_Label.grid(column=1, row=3, sticky="w")
        self.key_speed_units_Label = ttk.Label(
            self.cw_Info_Frame, name="key_speed_units_label")
        self.key_speed_units_Label.configure(
            style="Heading3b.TLabel", text='wpm')
        self.key_speed_units_Label.grid(column=2, row=3, sticky="w")
        self.delay_returning_to_rx_Label = ttk.Label(
            self.cw_Info_Frame, name="delay_returning_to_rx_label")
        self.delay_returning_to_rx_Label.configure(
            style="Heading3b.TLabel", text='Delay->RX')
        self.delay_returning_to_rx_Label.grid(
            column=0, padx="0 3", row=5, sticky="w")
        self.delay_returning_to_rx_value_Label = ttk.Label(
            self.cw_Info_Frame, name="delay_returning_to_rx_value_label")
        self.delay_returning_to_rx_value_VAR = tk.StringVar(value='199')
        self.delay_returning_to_rx_value_Label.configure(
            style="Heading3b.TLabel",
            text='199',
            textvariable=self.delay_returning_to_rx_value_VAR)
        self.delay_returning_to_rx_value_Label.grid(
            column=1, row=5, sticky="w")
        self.delay_returning_to_rx_units_Label = ttk.Label(
            self.cw_Info_Frame, name="delay_returning_to_rx_units_label")
        self.delay_returning_to_rx_units_Label.configure(
            style="Heading3b.TLabel", text='ms')
        self.delay_returning_to_rx_units_Label.grid(
            column=2, row=5, sticky="w")
        self.delay_starting_tx_Label = ttk.Label(
            self.cw_Info_Frame, name="delay_starting_tx_label")
        self.delay_starting_tx_Label.configure(
            style="Heading3b.TLabel", text='Delay->TX')
        self.delay_starting_tx_Label.grid(column=0, row=4, sticky="w")
        self.delay_starting_tx_value_Label = ttk.Label(
            self.cw_Info_Frame, name="delay_starting_tx_value_label")
        self.delay_starting_tx_value_VAR = tk.StringVar(value='299')
        self.delay_starting_tx_value_Label.configure(
            style="Heading3b.TLabel",
            text='299',
            textvariable=self.delay_starting_tx_value_VAR)
        self.delay_starting_tx_value_Label.grid(column=1, row=4, sticky="w")
        self.delay_starting_tx_units_Label = ttk.Label(
            self.cw_Info_Frame, name="delay_starting_tx_units_label")
        self.delay_starting_tx_units_Label.configure(
            style="Heading3b.TLabel", text='ms')
        self.delay_starting_tx_units_Label.grid(column=2, row=4, sticky="w")
        self.cw_Info_Frame.pack(
            anchor="nw",
            expand=False,
            fill="x",
            padx="100 0",
            pady=20,
            side="left")
        self.cw_Info_Frame.bind("<1>", self.cwSettings_CB, add="")
        self.ATT_IFS_Adjust_Frame.pack(
            anchor="w",
            expand=True,
            fill="x",
            pady="50 0",
            side="top")
        self.configure(
            borderwidth=5,
            height=665,
            style="Normal.TFrame",
            width=850)
        # Layout for 'main_window' skipped in custom widget template.

    def settings_CB(self):
        pass

    def vfo_CB(self):
        pass

    def mode_lsb_CB(self):
        pass

    def mode_usb_CB(self):
        pass

    def mode_cwl_CB(self):
        pass

    def mode_cwu_CB(self):
        pass

    def band_up_CB(self):
        pass

    def band_down_CB(self):
        pass

    def lock_CB(self):
        pass

    def speaker_CB(self):
        pass

    def stop_CB(self):
        pass

    def tuning_Preset_Select_CB(self):
        pass

    def split_CB(self):
        pass

    def rit_CB(self):
        pass

    def store_CB(self):
        pass

    def recall_CB(self):
        pass

    def tuning_Preset_5_CB(self):
        pass

    def tuning_Preset_4_CB(self):
        pass

    def tuning_Preset_3_CB(self):
        pass

    def tuning_Preset_2_CB(self):
        pass

    def tuning_Preset_1_CB(self):
        pass

    def tuning_Jogwheel_CB(self):
        pass

    def tuning_Multiplier_Button_CB(self):
        pass

    def updateATTValue_CB(self):
        pass

    def ATT_Jogwheel_ButtonPressed_CB(self, event=None):
        pass

    def ATT_Jogwheel_ButtonReleased_CB(self, event=None):
        pass

    def updateIFSValue_CB(self):
        pass

    def IFS_Jogwheel_ButtonPressed_CB(self, event=None):
        pass

    def IFS_Jogwheel_ButtonReleased_CB(self, event=None):
        pass

    def cwSettings_CB(self, event=None):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = piCECNextionUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

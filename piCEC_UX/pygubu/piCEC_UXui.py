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
class piCECNextionUI(tk.Tk):
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

        self.frame1 = ttk.Frame(self)
        self.frame1.configure(borderwidth=5, height=480, width=800)
        # First object created
        on_first_object_cb(self.frame1)

        self.menuBar_Frame = ttk.Frame(self.frame1, name="menubar_frame")
        self.menuBar_Frame.configure(height=50, width=800)
        self.txStop_Button = ttk.Menubutton(
            self.menuBar_Frame, name="txstop_button")
        self.txStop_Button.configure(text='TX STOP', width=8)
        self.txStop_Button.grid(column=0, row=0)
        self.vfo_Toggle_button = ttk.Menubutton(
            self.menuBar_Frame, name="vfo_toggle_button")
        self.vfo_Toggle_button.configure(compound="none", text='VFO', width=7)
        self.vfo_Toggle_button.grid(column=1, row=0)
        self.band_Move_Down_Button = ttk.Menubutton(
            self.menuBar_Frame, name="band_move_down_button")
        self.band_Move_Down_Button.configure(
            compound="none", text='BAND Down', width=9)
        self.band_Move_Down_Button.grid(column=2, row=0)
        self.band_Move_Up1_Button = ttk.Menubutton(
            self.menuBar_Frame, name="band_move_up1_button")
        self.band_Move_Up1_Button.configure(
            compound="none", text='BAND Up', width=9)
        self.band_Move_Up1_Button.grid(column=3, row=0)
        self.mode_Select_Button = ttk.Menubutton(
            self.menuBar_Frame, name="mode_select_button")
        self.mode_Select_Button.configure(
            compound="none", text='MODE', width=7)
        self.mode_Select_Button.grid(column=4, row=0)
        self.lock_Button = ttk.Menubutton(
            self.menuBar_Frame, name="lock_button")
        self.lock_Button.configure(compound="none", text='LOCK', width=7)
        self.lock_Button.grid(column=5, row=0)
        self.spk_or_SDR_button = ttk.Menubutton(
            self.menuBar_Frame, name="spk_or_sdr_button")
        self.spk_or_SDR_button.configure(compound="none", text='SPK', width=6)
        self.spk_or_SDR_button.grid(column=6, row=0)
        self.menuBar_Frame.pack(anchor="nw", fill="both", side="top")
        self.vfoA_Frame = ttk.Frame(self.frame1, name="vfoa_frame")
        self.vfoA_Frame.configure(width=480)
        self.rxTX_Status_Frame = ttk.Frame(
            self.vfoA_Frame, name="rxtx_status_frame")
        self.rxTX_Status_Frame.configure(height=200, width=200)
        self.rx_Status_Light_Label = ttk.Label(
            self.rxTX_Status_Frame, name="rx_status_light_label")
        self.rx_Status_Light_Label.configure(
            borderwidth=4, style="Heading1.TLabel", text='RX', width=5)
        self.rx_Status_Light_Label.grid(column=0, pady=15, row=0)
        self.tx_Status_Light_Label = ttk.Label(
            self.rxTX_Status_Frame, name="tx_status_light_label")
        self.tx_Status_Light_Label.configure(
            background="#000000",
            foreground="#ff2600",
            state="disabled",
            text='TX',
            width=5)
        self.tx_Status_Light_Label.grid(column=0, row=1)
        self.rxTX_Status_Frame.grid(column=0, padx=15, row=0, sticky="ew")
        self.vfo_Display = ttk.Frame(self.vfoA_Frame, name="vfo_display")
        self.vfo_Display.configure(height=200, width=200)
        self.vfo_Display.grid(column=1, row=0)
        self.vfoA_Frame.pack(anchor="nw", expand=True, fill="x", side="top")
        self.vfoB_Frame = ttk.Frame(self.frame1, name="vfob_frame")
        self.vfoB_Frame.configure(width=480)
        self.vfo_Frame = ttk.Frame(self.vfoB_Frame, name="vfo_frame")
        self.vfo_Frame.configure(height=200, width=200)
        self.vfo_Frame.grid(column=0, row=0)
        self.tuning_Step_Frame = ttk.Frame(
            self.vfoB_Frame, name="tuning_step_frame")
        self.tuning_Step_Frame.configure(height=200, width=200)
        self.tuning_Step_Frame.grid(column=1, row=0)
        self.vfoB_Frame.pack(side="top")
        self.att_IFS_Toggle_Frame = ttk.Frame(
            self.frame1, name="att_ifs_toggle_frame")
        self.att_IFS_Toggle_Frame.configure(height=200, width=200)
        self.signal_Control_Frame = ttk.Frame(
            self.att_IFS_Toggle_Frame, name="signal_control_frame")
        self.signal_Control_Frame.configure(height=200, width=200)
        self.signal_Control_Frame.grid(column=0, row=0)
        self.callsign_Frame = ttk.Frame(
            self.att_IFS_Toggle_Frame,
            name="callsign_frame")
        self.callsign_Frame.configure(height=200, width=200)
        self.callsign_Frame.grid(column=1, row=0)
        self.sw_Release_Frame = ttk.Frame(
            self.att_IFS_Toggle_Frame,
            name="sw_release_frame")
        self.sw_Release_Frame.configure(height=200, width=200)
        self.sw_Release_Frame.grid(column=2, row=0)
        self.att_IFS_Toggle_Frame.pack(side="top")
        self.sMeter_Frame = ttk.Frame(self.frame1, name="smeter_frame")
        self.sMeter_Frame.configure(height=200, width=200)
        self.sMeter_Frame.pack(side="top")
        self.ATT_IFS_Adjust_Frame = ttk.Frame(
            self.frame1, name="att_ifs_adjust_frame")
        self.ATT_IFS_Adjust_Frame.configure(height=200, width=200)
        self.cw_Info_Frame = ttk.Frame(
            self.ATT_IFS_Adjust_Frame,
            name="cw_info_frame")
        self.cw_Info_Frame.configure(height=200, width=200)
        self.cw_Info_Frame.grid(column=0, row=0)
        self.att_Graph_Frame = ttk.Frame(
            self.ATT_IFS_Adjust_Frame,
            name="att_graph_frame")
        self.att_Graph_Frame.configure(height=200, width=200)
        self.att_Graph_Frame.grid(column=1, row=0)
        self.ifs_Graph_Frame = ttk.Frame(
            self.ATT_IFS_Adjust_Frame,
            name="ifs_graph_frame")
        self.ifs_Graph_Frame.configure(height=200, width=200)
        self.ifs_Graph_Frame.grid(column=2, row=0)
        self.cw_Button_Frame = ttk.Frame(
            self.ATT_IFS_Adjust_Frame,
            name="cw_button_frame")
        self.cw_Button_Frame.configure(height=200, width=200)
        self.cw_Button_Frame.grid(column=3, row=0)
        self.ATT_IFS_Adjust_Frame.pack(side="top")
        self.frame1.pack(anchor="nw", expand=True, fill="both", side="top")
        self.configure(height=480, width=800)


if __name__ == "__main__":
    root = tk.Tk()
    widget = piCECNextionUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

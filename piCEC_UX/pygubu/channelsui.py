#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from frequencyChannel import frequencyChannel
from pygubu.widgets.combobox import Combobox
from pygubu.widgets.scrolledframe import ScrolledFrame


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
class channelsUI(tk.Toplevel):
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
            style="Heading2.TLabelframe",
            text='Frequency Channels',
            width=500)
        # First object created
        on_first_object_cb(labelframe1)

        frame1 = ttk.Frame(labelframe1)
        frame1.configure(style="Normal.TFrame", width=200)
        self.display_Current_VFO_Frame = ttk.Frame(
            frame1, name="display_current_vfo_frame")
        self.display_Current_VFO_Frame.configure(
            height=24, style="Normal.TFrame", width=450)
        self.current_VFO_Heading_Label = ttk.Label(
            self.display_Current_VFO_Frame,
            name="current_vfo_heading_label")
        self.current_VFO_Heading_Label.configure(
            style="Heading1b.TLabel", text='Current VFO:')
        self.current_VFO_Heading_Label.pack(
            anchor="center", padx="75 0", side="left")
        self.channel_Text_Label = ttk.Label(
            self.display_Current_VFO_Frame,
            name="channel_text_label")
        self.channel_Text_Label.configure(
            style="Heading2b.TLabel", text='Channel:')
        self.channel_Text_Label.pack(padx="10 0", side="left")
        self.current_Channel = ttk.Label(
            self.display_Current_VFO_Frame,
            name="current_channel")
        self.current_Channel_VAR = tk.StringVar(value='Not Saved')
        self.current_Channel.configure(
            style="Heading2bi.TLabel",
            text='Not Saved',
            textvariable=self.current_Channel_VAR,
            width=10)
        self.current_Channel.pack(padx="5 0", side="left")
        self.current_VFO_Label = ttk.Label(
            self.display_Current_VFO_Frame,
            name="current_vfo_label")
        self.current_VFO_VAR = tk.StringVar(value='99.999.99')
        self.current_VFO_Label.configure(
            style="Heading2b.TLabel",
            text='99.999.99',
            textvariable=self.current_VFO_VAR)
        self.current_VFO_Label.pack(padx="10 0", side="left")
        self.current_Mode_Label = ttk.Label(
            self.display_Current_VFO_Frame,
            name="current_mode_label")
        self.current_Mode_VAR = tk.StringVar(value='CWL')
        self.current_Mode_Label.configure(
            style="Heading2b.TLabel",
            text='CWL',
            textvariable=self.current_Mode_VAR)
        self.current_Mode_Label.pack(expand=False, padx="10 10", side="left")
        self.display_Current_VFO_Frame.grid(
            column=0, pady="15 0", row=0, sticky="new")
        self.header_Line_Frame = ttk.Frame(frame1, name="header_line_frame")
        self.header_Line_Frame.configure(
            height=24, style="Normal.TFrame", width=200)
        self.channel_header_Label = ttk.Label(
            self.header_Line_Frame, name="channel_header_label")
        self.channel_header_Label.configure(
            style="Heading2b.TLabel", text='Channel')
        self.channel_header_Label.grid(column=0, padx="106 0", row=0)
        self.name_Header_Label = ttk.Label(
            self.header_Line_Frame, name="name_header_label")
        self.name_Header_Label.configure(style="Heading2b.TLabel", text='Name')
        self.name_Header_Label.grid(column=1, padx="28 0", row=0)
        self.frequency_Header_Label = ttk.Label(
            self.header_Line_Frame, name="frequency_header_label")
        self.frequency_Header_Label.configure(
            style="Heading2b.TLabel", text='Frequency')
        self.frequency_Header_Label.grid(column=2, padx="17 0", row=0)
        self.mode_Header_Label = ttk.Label(
            self.header_Line_Frame, name="mode_header_label")
        self.mode_Header_Label.configure(style="Heading2b.TLabel", text='Mode')
        self.mode_Header_Label.grid(column=4, padx="36 0", row=0)
        self.showLabel_Header_Label = ttk.Label(
            self.header_Line_Frame, name="showlabel_header_label")
        self.showLabel_Header_Label.configure(
            style="Heading2b.TLabel", text='Visible')
        self.showLabel_Header_Label.grid(column=5, padx="46 0", row=0)
        self.scan_Set_Label = ttk.Label(
            self.header_Line_Frame, name="scan_set_label")
        self.scan_Set_Label.configure(
            style="Heading2b.TLabel", text='Scan Set')
        self.scan_Set_Label.grid(column=6, padx="20 0", row=0)
        self.header_Line_Frame.grid(column=0, pady="20 0", row=1, sticky="new")
        self.scrolledChannelFrame = ScrolledFrame(
            frame1, scrolltype="both", name="scrolledchannelframe")
        self.scrolledChannelFrame.innerframe.configure(
            relief="raised", style="Normal.TFrame", width=500)
        self.scrolledChannelFrame.configure(usemousewheel=True)
        self.frequencyChannel1 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel1")
        self.frequencyChannel1.pack(side="top")
        self.frequencyChannel2 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel2")
        self.frequencyChannel2.pack(pady="10 0", side="top")
        self.frequencyChannel3 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel3")
        self.frequencyChannel3.pack(pady="10 0", side="top")
        self.frequencyChannel4 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel4")
        self.frequencyChannel4.pack(pady="10 0", side="top")
        self.frequencyChannel5 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel5")
        self.frequencyChannel5.pack(pady="10 0", side="top")
        self.frequencyChannel6 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel6")
        self.frequencyChannel6.pack(pady="10 0", side="top")
        self.frequencyChannel7 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel7")
        self.frequencyChannel7.pack(pady="10 0", side="top")
        self.frequencyChannel8 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel8")
        self.frequencyChannel8.pack(pady="10 0", side="top")
        self.frequencyChannel9 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel9")
        self.frequencyChannel9.pack(pady="10 0", side="top")
        self.frequencyChannel10 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel10")
        self.frequencyChannel10.pack(pady="10 0", side="top")
        self.frequencyChannel11 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel11")
        self.frequencyChannel11.pack(pady="10 0", side="top")
        self.frequencyChannel12 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel12")
        self.frequencyChannel12.pack(pady="10 0", side="top")
        self.frequencyChannel13 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel13")
        self.frequencyChannel13.pack(pady="10 0", side="top")
        self.frequencyChannel14 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel14")
        self.frequencyChannel14.pack(pady="10 0", side="top")
        self.frequencyChannel15 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel15")
        self.frequencyChannel15.pack(pady="10 0", side="top")
        self.frequencyChannel16 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel16")
        self.frequencyChannel16.pack(pady="10 0", side="top")
        self.frequencyChannel17 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel17")
        self.frequencyChannel17.pack(pady="10 0", side="top")
        self.frequencyChannel18 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel18")
        self.frequencyChannel18.pack(pady="10 0", side="top")
        self.frequencyChannel19 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel19")
        self.frequencyChannel19.pack(pady="10 0", side="top")
        self.frequencyChannel20 = frequencyChannel(
            self.scrolledChannelFrame.innerframe, name="frequencychannel20")
        self.frequencyChannel20.pack(pady="10 0", side="top")
        self.scrolledChannelFrame.grid(
            column=0, pady="5 0", row=2, sticky="nsew")
        self.closingFrame = ttk.Frame(frame1, name="closingframe")
        self.closingFrame.configure(
            height=50,
            relief="raised",
            style="Normal.TFrame",
            width=200)
        self.go_Channel_Button = ttk.Button(
            self.closingFrame, name="go_channel_button")
        self.go_Channel_Button.configure(
            compound="none",
            state="normal",
            style="Button2b.TButton",
            text='QSY Channel')
        self.go_Channel_Button.grid(column=0, pady="2 0", row=0, sticky="ns")
        self.go_Channel_Button.configure(command=self.QSY_Channel_CB)
        self.save_Channel_Button = ttk.Button(
            self.closingFrame, name="save_channel_button")
        self.save_Channel_Button.configure(
            state="normal",
            style="Button2b.TButton",
            text='Save Channel')
        self.save_Channel_Button.grid(
            column=1, padx="10 0", pady="2 0", row=0, sticky="ns")
        self.save_Channel_Button.configure(command=self.save_Channel_CB)
        self.scan_Select_Combobox = Combobox(
            self.closingFrame, name="scan_select_combobox")
        self.scan_Select_Channel_VAR = tk.StringVar()
        self.scan_Select_Combobox.configure(
            justify="center",
            keyvariable=self.scan_Select_Channel_VAR,
            style="ComboBox2b.TCombobox",
            values='None Scan1 Scan2 Scan3 Scan4',
            width=5)
        self.scan_Select_Combobox.grid(
            column=2, padx="10 0", row=0, sticky="ns")
        self.scan_Button = ttk.Button(self.closingFrame, name="scan_button")
        self.scan_Channel_VAR = tk.StringVar(value='Scan')
        self.scan_Button.configure(
            style="Button2b.TButton",
            text='Scan',
            textvariable=self.scan_Channel_VAR)
        self.scan_Button.grid(
            column=3,
            padx="10 0",
            pady="2 0",
            row=0,
            sticky="ns")
        self.scan_Button.configure(command=self.scan_Channel_CB)
        self.refresh_Button = ttk.Button(
            self.closingFrame, name="refresh_button")
        self.refresh_Button.configure(style="Button2b.TButton", text='Refresh')
        self.refresh_Button.grid(
            column=5,
            padx="10 0",
            pady="2 0",
            row=0,
            sticky="ns")
        self.refresh_Button.configure(command=self.refresh_Channel_CB)
        self.close_Button = ttk.Button(self.closingFrame, name="close_button")
        self.close_Button.configure(style="Button2b.TButton", text='Close')
        self.close_Button.grid(
            column=6,
            padx="10 0",
            pady="2 0",
            row=0,
            sticky="ns")
        self.close_Button.configure(command=self.close_Channel_CB)
        self.closingFrame.grid(column=0, padx=15, pady=15, row=3, sticky="ew")
        frame1.pack(expand=True, fill="both", side="top")
        frame1.rowconfigure(2, minsize=400)
        labelframe1.pack(expand=True, fill="both", side="top")
        labelframe1.pack_propagate(0)
        self.configure(height=575, width=600)
        self.geometry("600x575")
        # Layout for 'channels_Window' skipped in custom widget template.

    def QSY_Channel_CB(self):
        pass

    def save_Channel_CB(self):
        pass

    def scan_Channel_CB(self):
        pass

    def refresh_Channel_CB(self):
        pass

    def close_Channel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelsUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

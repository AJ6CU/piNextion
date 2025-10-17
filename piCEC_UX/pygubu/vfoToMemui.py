#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from channelWrite10PlusFrame import channelWrite10PlusFrame
from channelWriteFrame import channelWriteFrame
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
class vfoToMemUI(tk.Toplevel):
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
            text='VFO->Memory',
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
        self.display_Current_VFO_Frame.pack(
            anchor="center", expand=False, fill="x", padx=10, pady="10 0")
        scrolledframe2 = ScrolledFrame(frame1, scrolltype="both")
        scrolledframe2.innerframe.configure(
            height=350,
            relief="raised",
            style="Normal.TFrame",
            takefocus=True,
            width=500)
        scrolledframe2.configure(usemousewheel=True)
        self.channel_Write_1_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_1_frame")
        self.channel_Write_1_Frame.pack(side="top")
        self.channel_Write_2_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_2_frame")
        self.channel_Write_2_Frame.pack(pady="5 0", side="top")
        self.channel_Write_3_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_3_frame")
        self.channel_Write_3_Frame.pack(pady="5 0", side="top")
        self.channel_Write_4_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_4_frame")
        self.channel_Write_4_Frame.pack(pady="5 0", side="top")
        self.channel_Write_5_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_5_frame")
        self.channel_Write_5_Frame.pack(pady="5 0", side="top")
        self.channel_Write_6_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_6_frame")
        self.channel_Write_6_Frame.pack(pady="5 0", side="top")
        self.channel_Write_7_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_7_frame")
        self.channel_Write_7_Frame.pack(pady="5 0", side="top")
        self.channel_Write_8_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_8_frame")
        self.channel_Write_8_Frame.pack(pady="5 0", side="top")
        self.channel_Write_9_Frame = channelWriteFrame(
            scrolledframe2.innerframe, name="channel_write_9_frame")
        self.channel_Write_9_Frame.pack(pady="5 0", side="top")
        self.channel_Write_10_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_10_frame")
        self.channel_Write_10_Frame.pack(pady="5 0", side="top")
        self.channel_Write_11_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_11_frame")
        self.channel_Write_11_Frame.pack(pady="5 0", side="top")
        self.channel_Write_12_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_12_frame")
        self.channel_Write_12_Frame.pack(pady="5 0", side="top")
        self.channel_Write_13_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_13_frame")
        self.channel_Write_13_Frame.pack(pady="5 0", side="top")
        self.channel_Write_14_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_14_frame")
        self.channel_Write_14_Frame.pack(pady="5 0", side="top")
        self.channel_Write_15_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_15_frame")
        self.channel_Write_15_Frame.pack(pady="5 0", side="top")
        self.channel_Write_16_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_16_frame")
        self.channel_Write_16_Frame.pack(pady="5 0", side="top")
        self.channel_Write_17_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_17_frame")
        self.channel_Write_17_Frame.pack(pady="5 0", side="top")
        self.channel_Write_18_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_18_frame")
        self.channel_Write_18_Frame.pack(pady="5 0", side="top")
        self.channel_Write_19_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_19_frame")
        self.channel_Write_19_Frame.pack(pady="5 0", side="top")
        self.channel_Write_20_Frame = channelWrite10PlusFrame(
            scrolledframe2.innerframe, name="channel_write_20_frame")
        self.channel_Write_20_Frame.pack(pady="5 0", side="top")
        scrolledframe2.pack(
            anchor="center",
            expand=True,
            fill="both",
            pady="20 0")
        self.closingFrame = ttk.Frame(frame1, name="closingframe")
        self.closingFrame.configure(
            height=50, style="Normal.TFrame", width=200)
        self.apply_Button = ttk.Button(self.closingFrame, name="apply_button")
        self.apply_Button.configure(style="Button2b.TButton", text='Write')
        self.apply_Button.pack(anchor="center", padx=10, side="left")
        self.apply_Button.configure(command=self.apply_CB)
        self.cancel_Buttom = ttk.Button(
            self.closingFrame, name="cancel_buttom")
        self.cancel_Buttom.configure(style="Button2b.TButton", text='Close')
        self.cancel_Buttom.pack(anchor="center", padx=10, side="left")
        self.cancel_Buttom.configure(command=self.cancel_CB)
        self.closingFrame.pack(pady=20, side="bottom")
        frame1.pack(expand=True, fill="both", side="top")
        frame1.pack_propagate(0)
        labelframe1.pack(expand=True, fill="both", side="top")
        labelframe1.pack_propagate(0)
        self.configure(height=450, width=600)
        # Layout for 'vfo_to_mem' skipped in custom widget template.

    def apply_CB(self):
        pass

    def cancel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = vfoToMemUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from channelFrame import channelFrame
from channelFrame10Plus import channelFrame10Plus
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
class memToVFOUI(tk.Toplevel):
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

        self.labelframe1 = ttk.Labelframe(self)
        self.labelframe1.configure(
            height=400,
            style="Heading2.TLabelframe",
            text='Memory -> VFO',
            width=500)
        # First object created
        on_first_object_cb(self.labelframe1)

        self.frame1 = ttk.Frame(self.labelframe1)
        self.frame1.configure(height=200, style="Normal.TFrame", width=200)
        self.display_Current_VFO_Frame = ttk.Frame(
            self.frame1, name="display_current_vfo_frame")
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
        self.scrolledMemoryFrame = ScrolledFrame(
            self.frame1, scrolltype="both", name="scrolledmemoryframe")
        self.scrolledMemoryFrame.innerframe.configure(
            height=350, relief="raised", style="Normal.TFrame", width=500)
        self.scrolledMemoryFrame.configure(usemousewheel=True)
        self.channelFrame1 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe1")
        self.channelFrame1.pack(pady="0 15", side="top")
        self.channelFrame2 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe2")
        self.channelFrame2.pack(pady="0 15", side="top")
        self.channelFrame3 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe3")
        self.channelFrame3.pack(pady="0 15", side="top")
        self.channelFrame4 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe4")
        self.channelFrame4.pack(pady="0 15", side="top")
        self.channelFrame5 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe5")
        self.channelFrame5.pack(pady="0 15", side="top")
        self.channelFrame6 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe6")
        self.channelFrame6.pack(pady="0 15", side="top")
        self.channelFrame7 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe7")
        self.channelFrame7.pack(pady="0 15", side="top")
        self.channelFrame8 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe8")
        self.channelFrame8.pack(pady="0 15", side="top")
        self.channelFrame9 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe9")
        self.channelFrame9.pack(pady="0 15", side="top")
        self.channelFrame10 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe10")
        self.channelFrame10.pack(pady="0 15", side="top")
        self.channelFrame11 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe11")
        self.channelFrame11.pack(pady="0 15", side="top")
        self.channelFrame12 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe12")
        self.channelFrame12.pack(pady="0 15", side="top")
        self.channelFrame13 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe13")
        self.channelFrame13.pack(pady="0 15", side="top")
        self.channelFrame14 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe14")
        self.channelFrame14.pack(pady="0 15", side="top")
        self.channelFrame15 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe15")
        self.channelFrame15.pack(pady="0 15", side="top")
        self.channelFrame16 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe16")
        self.channelFrame16.pack(pady="0 15", side="top")
        self.channelFrame17 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe17")
        self.channelFrame17.pack(pady="0 15", side="top")
        self.channelFrame18 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe18")
        self.channelFrame18.pack(pady="0 15", side="top")
        self.channelFrame19 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe19")
        self.channelFrame19.pack(pady="0 15", side="top")
        self.channelFrame20 = channelFrame10Plus(
            self.scrolledMemoryFrame.innerframe, name="channelframe20")
        self.channelFrame20.pack(pady="0 15", side="top")
        self.scrolledMemoryFrame.pack(
            anchor="center",
            expand=True,
            fill="both",
            pady="20 0",
            side="top")
        self.closingFrame = ttk.Frame(self.frame1, name="closingframe")
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
            side="bottom")
        self.frame1.pack(expand=True, fill="both", side="top")
        self.frame1.pack_propagate(0)
        self.labelframe1.pack(expand=True, fill="both", side="top")
        self.labelframe1.pack_propagate(0)
        self.configure(height=450, width=600)
        # Layout for 'mem_to_VFO_Window' skipped in custom widget template.

    def apply_CB(self):
        pass

    def cancel_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = memToVFOUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

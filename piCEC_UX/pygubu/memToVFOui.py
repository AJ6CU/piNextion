#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from channelFrame import channelFrame
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
            width=300)
        # First object created
        on_first_object_cb(self.labelframe1)

        self.scrolledMemoryFrame = ScrolledFrame(
            self.labelframe1, scrolltype="both", name="scrolledmemoryframe")
        self.scrolledMemoryFrame.innerframe.configure(
            style="Normal.TFrame", width=400)
        self.scrolledMemoryFrame.configure(usemousewheel=False)
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
        self.channelframe8 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe8")
        self.channelframe8.pack(pady="0 15", side="top")
        self.channelframe9 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe9")
        self.channelframe9.pack(pady="0 15", side="top")
        self.channelframe10 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe10")
        self.channelframe10.pack(pady="0 15", side="top")
        self.channelFrame11 = channelFrame(
            self.scrolledMemoryFrame.innerframe,
            name="channelframe11")
        self.channelFrame11.pack(side="top")
        self.scrolledMemoryFrame.pack(expand=True, fill="x", side="top")
        self.closingFrame = ttk.Frame(self.labelframe1, name="closingframe")
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
        self.labelframe1.pack(expand=True, fill="both", side="top")
        self.configure(height=400, width=400)
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

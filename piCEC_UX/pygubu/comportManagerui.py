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
class comportManagerUI(ttk.Frame):
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

        self.comportMessage_Frame = ttk.Frame(
            self, name="comportmessage_frame")
        self.comportMessage_Frame.configure(
            height=150, style="Normal.TFrame", width=200)
        # First object created
        on_first_object_cb(self.comportMessage_Frame)

        label1 = ttk.Label(self.comportMessage_Frame)
        label1.configure(
            style="Heading1b.TLabel",
            text='Connect to Your uBITX')
        label1.pack(side="top")
        label3 = ttk.Label(self.comportMessage_Frame)
        label3.configure(
            anchor="w",
            justify="left",
            style="Heading2b.TLabel",
            text='The serial port connecting your uBITX to\nthis software is either unspecified or not\nworking. You must specify the correct \nport below before proceeding.',
            width=300)
        label3.pack(pady=20, side="top")
        self.comportMessage_Frame.pack(
            expand=True, fill="both", padx=10, pady=10, side="top")
        self.comportMessage_Frame.pack_propagate(0)
        frame1 = ttk.Frame(self)
        frame1.configure(
            height=200,
            relief="raised",
            style="NormalOutline.TFrame",
            width=200)
        self.selectComportTitle_Label = ttk.Label(
            frame1, name="selectcomporttitle_label")
        self.selectComportTitle_Label.configure(
            style="Heading2b.TLabel", text='Radio:')
        self.selectComportTitle_Label.pack(
            anchor="w", padx="10 0", pady=5, side="left")
        self.comportSelection_Frame = ttk.Frame(
            frame1, name="comportselection_frame")
        self.comportSelection_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.availableComPorts_VAR = tk.StringVar(value='Select Serial Port')
        __values = ['Select Serial Port']
        self.comPortsOptionMenu = ttk.OptionMenu(
            self.comportSelection_Frame,
            self.availableComPorts_VAR,
            "Select Serial Port",
            *__values,
            command=self.radioSerialPortSelected_CB)
        self.comPortsOptionMenu.pack(side="left")
        self.comPortListRefresh = tk.Button(
            self.comportSelection_Frame,
            name="comportlistrefresh")
        self.comPortListRefresh.configure(
            bitmap="error",
            borderwidth=0,
            cursor="arrow",
            font="TkDefaultFont")
        self.comPortListRefresh.pack(padx=10, side="left")
        self.comPortListRefresh.configure(command=self.updateComPorts)
        self.comportSelection_Frame.pack(
            expand=True, fill="x", padx=10, pady=5, side="top")
        frame1.pack(expand=True, fill="x", padx=10, pady="0 20", side="bottom")
        self.configure(height=100, style="Normal.TFrame", width=278)
        # Layout for 'selectComPortFrame' skipped in custom widget template.

    def radioSerialPortSelected_CB(self, option):
        pass

    def updateComPorts(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = comportManagerUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

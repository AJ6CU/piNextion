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
            height=400,
            style="Heading2.TLabelframe",
            text='VFO->Memory',
            width=600)
        # First object created
        on_first_object_cb(labelframe1)

        frame1 = ttk.Frame(labelframe1)
        frame1.configure(height=200, style="Normal.TFrame", width=200)
        self.VFO_To_Mem_Frame = ttk.Frame(frame1, name="vfo_to_mem_frame")
        self.VFO_To_Mem_Frame.configure(
            height=200, style="Normal.TFrame", width=200)
        self.VFO_to_Mem_Label = ttk.Label(
            self.VFO_To_Mem_Frame, name="vfo_to_mem_label")
        self.VFO_to_Mem_Label.configure(
            style="Heading4.TLabel", text='Delete Me\n')
        self.VFO_to_Mem_Label.grid(column=0, row=2, sticky="w")
        self.VFO_To_Mem_Freq_Entry = ttk.Entry(
            self.VFO_To_Mem_Frame, name="vfo_to_mem_freq_entry")
        self.VFO_To_Mem_Freq_Entry.configure(
            justify="right",
            style="Normal.TEntry",
            validate="none",
            width=10)
        _text_ = '599'
        self.VFO_To_Mem_Freq_Entry.delete("0", "end")
        self.VFO_To_Mem_Freq_Entry.insert("0", _text_)
        self.VFO_To_Mem_Freq_Entry.grid(column=1, row=2)
        self.VFO_To_Mem_Frame.pack(padx="50 0", side="top")
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

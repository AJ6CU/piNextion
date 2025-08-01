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
class modeSelectUI(tk.Toplevel):
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

        self.lsb_select_Button = ttk.Button(self, name="lsb_select_button")
        self.lsb_select_Button.configure(text='LSB')
        # First object created
        on_first_object_cb(self.lsb_select_Button)

        self.lsb_select_Button.pack(anchor="w", side="left")
        self.lsb_select_Button.configure(command=self.lsb_clicked_CB)
        self.usb_select_Button = ttk.Button(self, name="usb_select_button")
        self.usb_select_Button.configure(text='USB')
        self.usb_select_Button.pack(anchor="w", side="left")
        self.cwl_select_Button = ttk.Button(self, name="cwl_select_button")
        self.cwl_select_Button.configure(text='CWL')
        self.cwl_select_Button.pack(anchor="w", side="left")
        self.cwu_select_Button = ttk.Button(self, name="cwu_select_button")
        self.cwu_select_Button.configure(text='CWU')
        self.cwu_select_Button.pack(anchor="w", side="left")
        self.configure(height=200, width=200)

    def lsb_clicked_CB(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = modeSelectUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

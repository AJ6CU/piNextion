#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk



def i18n_translator_noop(value):
    """i18n - Setup translator in derived class file"""
    return value


def first_object_callback_noop(widget):
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
class testButtonClassUI(ttk.Frame):
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

        self.button1 = ttk.Button(self)
        self.button1.configure(style="Button3Blue.TButton", text='button1')
        # First object created
        on_first_object_cb(self.button1)

        self.button1.pack(side="top")
        self.configure(height=200, style="Normal.TFrame", width=200)
        self.pack(side="top")


if __name__ == "__main__":
    root = tk.Tk()
    widget = testButtonClassUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

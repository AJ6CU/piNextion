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
class testMe1UI(tk.Tk):
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

        frame1 = ttk.Frame(self)
        frame1.configure(height=200, width=200)
        # First object created
        on_first_object_cb(frame1)

        button1 = ttk.Button(frame1)
        button1.configure(text='button1')
        button1.pack(side="top")
        button1.configure(command=self.pushed)
        frame1.pack(side="top")
        self.configure(height=200, width=200)

    def pushed(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = testMe1UI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

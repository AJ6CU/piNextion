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
class channelFrame10PlusUI(ttk.Frame):
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

        self.Go_Button = ttk.Button(self, name="go_button")
        self.go_Button_Text_VAR = tk.StringVar(value='QSY')
        self.Go_Button.configure(
            style="Button2b.TButton",
            text='QSY',
            textvariable=self.go_Button_Text_VAR,
            width=8)
        # First object created
        on_first_object_cb(self.Go_Button)

        self.Go_Button.grid(column=0, row=0, sticky="w")
        self.Go_Button.configure(command=self.mem_go_button)
        self.channel_Label = ttk.Label(self, name="channel_label")
        self.Label_VAR = tk.StringVar(value='Channel 11')
        self.channel_Label.configure(
            style="Heading2bi.TLabel",
            text='Channel 11',
            textvariable=self.Label_VAR,
            width=12)
        self.channel_Label.grid(column=1, padx="10 0", row=0, sticky="w")
        self.freq_label = ttk.Label(self, name="freq_label")
        self.Freq_VAR = tk.StringVar(value='99.999.999')
        self.freq_label.configure(
            style="Heading2b.TLabel",
            text='99.999.999',
            textvariable=self.Freq_VAR,
            width=10)
        self.freq_label.grid(column=2, padx="10 0", row=0, sticky="w")
        self.mode_Label = ttk.Label(self, name="mode_label")
        self.Mode_VAR = tk.StringVar(value='CWL')
        self.mode_Label.configure(
            style="Heading2b.TLabel",
            text='CWL',
            textvariable=self.Mode_VAR,
            width=5)
        self.mode_Label.grid(column=3, padx="10 0", row=0, sticky="w")
        self.configure(height=200, style="Normal.TFrame", width=200)
        # Layout for 'channelFrame10Plus' skipped in custom widget template.

    def mem_go_button(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    widget = channelFrame10PlusUI(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()

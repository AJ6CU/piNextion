###################--------------TkDial-Jogwheel--------------###################
# URL = https://github.com/Akascape/TkDial/blob/main/tkdial/jogwheel.py
# Part of TKDial

import tkinter.ttk as ttk

from Jogwheel import Jogwheel

class JogwheelCustom(Jogwheel):
    def __init__(self, master=None, **kw):

        self.foregroundColor={"normal":ttk.Style().lookup(master.cget('style'),'foreground'),
                              "disabled":ttk.Style().lookup(master.cget('style'),'background')
                              }
        self.textColor={    "normal":ttk.Style().lookup(master.cget('style'),'foreground'),
                            "disabled":"gray"
                              }
        self.buttonColor={  "normal":'yellow',
                            "disabled":"gray"
                              }

        self.scaleColor={"normal":'blue',
                         "disabled":"gray"
                         }
        self.initialValue = 0
        if "name" in kw:
            kw.pop("name")
        if "value" in kw:
            self.initialValue = kw.pop("value")

        super().__init__(master,
                        bg=ttk.Style().lookup(master.cget('style'),'background'),
                        fg=ttk.Style().lookup(master.cget('style'),'background'),
                        text_font=ttk.Style().lookup(master.cget('style'),'font'),
                        **kw
        )

        self.lastValue = self.initialValue
        self.set(self.lastValue)
        self.setStateDisabled()


    def setStateDisabled(self):
        self.configure(state="disabled", scroll=False)
        self.lastValue = self.get()
        self.configure( fg=self.foregroundColor["disabled"],
                        scale_color=self.scaleColor["disabled"],
                        button_color=self.buttonColor["disabled"],
                        text_color=self.textColor["disabled"]
                        )

    def setStateNormal(self):
        self.configure(state="normal", scroll=True)
        self.set(self.lastValue)
        self.configure( fg=self.foregroundColor["normal"],
                        scale_color=self.scaleColor["normal"],
                        button_color=self.buttonColor["normal"],
                        text_color=self.textColor["normal"]
                        )


    def configure(self, **kwargs):
        """
        This function contains some configurable options
        """

        if "text" in kwargs:
             self.itemconfigure(
                tagOrId="text",
                text=kwargs.pop("text"))

        if "start" in kwargs:
            self.start = kwargs.pop("start")

        if "end" in kwargs:
            self.end = kwargs.pop("end")

        if "bg" in kwargs:
            super().configure(bg=kwargs.pop("bg"))

        if "width" in kwargs:
            super().configure(width=kwargs.pop("width"))

        if "height" in kwargs:
            super().configure(height=kwargs.pop("height"))

        if "scale_color" in kwargs:
            self.itemconfigure(tagOrId="min_scale",
                    fill=kwargs['scale_color'])
            self.itemconfigure(
                tagOrId="progress",
                outline=kwargs.pop("scale_color"))

        if "fg" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                fill=kwargs.pop('fg'))

        if "text_color" in kwargs:
            self.itemconfigure(
                tagOrId="text",
                fill=kwargs.pop("text_color"))

        if "button_color" in kwargs:
            self.itemconfigure(
                tagOrId="needle",
                fill=kwargs.pop("button_color"))

        if "border_color" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                outline=kwargs.pop("border_color"))

        if "scroll_steps" in kwargs:
            self.scroll_steps = kwargs.pop("scroll_steps")

        if "scroll" in kwargs:
            if kwargs["scroll"]==False:
                super().unbind('<MouseWheel>')
                super().unbind('<Button-4>')
                super().unbind('<Button-5>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
                super().bind("<Button-4>", lambda e: self.scroll_command(-1))
                super().bind("<Button-5>", lambda e: self.scroll_command(1))
            kwargs.pop("scroll")

        if "integer" in kwargs:
            self.set(self.value)
            self.integer = kwargs.pop("integer")

        if "state" in kwargs:
            self.state = kwargs.pop("state")
            self.needle_state()
            if self.state == "normal":
                self.set(self.lastValue)
                self.configure(fg=self.foregroundColor["normal"],
                               scale_color=self.scaleColor["normal"],
                               button_color=self.buttonColor["normal"],
                               text_color=self.textColor["normal"]
                               )
            else:
                self.lastValue = self.get()
                self.configure(fg=self.foregroundColor["disabled"],
                               scale_color=self.scaleColor["disabled"],
                               button_color=self.buttonColor["disabled"],
                               text_color=self.textColor["disabled"]
                               )

        if "progress" in kwargs:
                self.progress = kwargs.pop("progress")

        if "command" in kwargs:
            self.command = kwargs.pop("command")

        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])

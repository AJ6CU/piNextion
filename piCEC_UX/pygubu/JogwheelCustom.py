###################--------------TkDial-Jogwheel--------------###################
# URL = https://github.com/Akascape/TkDial/blob/main/tkdial/jogwheel.py
# Part of TKDial

# import tkinter as ttk
import tkinter.ttk as ttk

from tkdial import Jogwheel

class JogwheelCustom(Jogwheel):
    def __init__(self, master=None, **kw):
        # self.backgroundColor={"normal":ttk.Style().lookup(master.cget('style'),'background'),
        #                       "disabled":"black"
        #                       }
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
        super().__init__(master,
                        radius=200,
                        start=-0,
                        end=255,
                        scroll_steps=10,
                        bg=ttk.Style().lookup(master.cget('style'),'background'),
                        fg=ttk.Style().lookup(master.cget('style'),'background'),
                        text_font=ttk.Style().lookup(master.cget('style'),'font'),
                        button_radius=25
        )

        self.lastValue = None
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

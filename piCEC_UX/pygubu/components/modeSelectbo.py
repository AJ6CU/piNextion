#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from modeSelect import modeSelect


#
# Builder definition section
#

class modeSelectBO(BuilderObject):
    class_ = modeSelect


_builder_id = "projectcustom.modeSelect"
register_widget(
    _builder_id, modeSelectBO, "modeSelect", ("ttk", "Project Widgets")
)

#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.combobox import Combobox
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from channelWriteFrame import channelWriteFrame


#
# Builder definition section
#

class channelWriteFrameBO(BuilderObject):
    class_ = channelWriteFrame


_builder_id = "projectcustom.channelWriteFrame"
register_widget(
    _builder_id, channelWriteFrameBO, "channelWriteFrame", (
        "ttk", "Project Widgets")
)

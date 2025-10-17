#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.combobox import Combobox
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from channelWrite10PlusFrame import channelWrite10PlusFrame


#
# Builder definition section
#

class channelWrite10PlusFrameBO(BuilderObject):
    class_ = channelWrite10PlusFrame


_builder_id = "projectcustom.channelWrite10PlusFrame"
register_widget(
    _builder_id, channelWrite10PlusFrameBO, "channelWrite10PlusFrame", (
        "ttk", "Project Widgets")
)

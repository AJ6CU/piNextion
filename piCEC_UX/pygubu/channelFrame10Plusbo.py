#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from channelFrame10Plus import channelFrame10Plus


#
# Builder definition section
#

class channelFrame10PlusBO(BuilderObject):
    class_ = channelFrame10Plus


_builder_id = "projectcustom.channelFrame10Plus"
register_widget(
    _builder_id, channelFrame10PlusBO, "channelFrame10Plus", (
        "ttk", "Project Widgets")
)

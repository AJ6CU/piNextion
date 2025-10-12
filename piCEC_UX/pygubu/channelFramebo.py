#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from channelFrame import channelFrame


#
# Builder definition section
#

class channelFrameBO(BuilderObject):
    class_ = channelFrame

_builder_id = "projectcustom.channelFrame"
register_widget(
    _builder_id, channelFrameBO, "channelFrame", ("ttk", "Project Widgets")
)

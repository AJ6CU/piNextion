#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from settingsMisc import settingsMisc


#
# Builder definition section
#
_widget_namespace = "settingsMisc"
_widget_classname = "settingsMisc"
_builder_namespace = "projectcustom"
_section_name = "Project Widgets"


class settingsMiscBO(BuilderObject):
    class_ = settingsMisc


_builder_id = f"{_builder_namespace}.{_widget_classname}"
register_widget(
    _builder_id, settingsMiscBO, _widget_classname, ("ttk", _section_name)
)

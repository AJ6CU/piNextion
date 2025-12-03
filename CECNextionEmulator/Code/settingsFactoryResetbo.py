#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from settingsFactoryReset import settingsFactoryReset


#
# Builder definition section
#
_widget_namespace = "settingsFactoryReset"
_widget_classname = "settingsFactoryReset"
_builder_namespace = "projectcustom"
_section_name = "Project Widgets"


class settingsFactoryResetBO(BuilderObject):
    class_ = settingsFactoryReset


_builder_id = f"{_builder_namespace}.{_widget_classname}"
register_widget(
    _builder_id, settingsFactoryResetBO, _widget_classname, (
        "ttk", _section_name)
)

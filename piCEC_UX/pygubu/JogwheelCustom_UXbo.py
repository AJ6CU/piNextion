import tkinter as tk


from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from JogwheelCustom import JogwheelCustom

#
# Builder definition section
#

class JogwheelCustom_UXbo(BuilderObject):
    class_ = JogwheelCustom


_builder_id = "projectcustom.Jogwheel"
register_widget(
    _builder_id, JogwheelCustom_UXbo, "Jogwheel", ("tk", "Project Widgets")
)

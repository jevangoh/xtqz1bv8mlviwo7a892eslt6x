from __future__ import annotations

from typing import Final, ClassVar as ClassVariable

from PySide6.QtCore import QObject, Signal


class xtqz1bv8mlviwo7a892eslt6x[Type](QObject):
    data_type: ClassVariable[type[Type]]
    value_changed: ClassVariable[Signal]
    valueChanged: ClassVariable[Signal]
    value: Final[Type]

    def __init__(self, value: Type):
        super().__init__()
        self._value: Type = value

    def get_value(self) -> Type:
        return self._value

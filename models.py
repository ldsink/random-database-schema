from dataclasses import dataclass

from constants import ColumnDataType


@dataclass
class DatabaseItem:
    name: str


@dataclass
class TableItem:
    name: str


@dataclass
class ColumnItem:
    name: str
    data_type: ColumnDataType
    null: bool = False
    default = None
    comment: str = None

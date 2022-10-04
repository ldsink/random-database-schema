from dataclasses import dataclass
from typing import List

from constants import ColumnDataType


@dataclass
class DatabaseItem:
    name: str


@dataclass
class TableColumnItem:
    name: str
    data_type: ColumnDataType
    null: bool = False
    default = None
    comment: str = None


@dataclass
class TableItem:
    database: DatabaseItem
    name: str
    columns: List[TableColumnItem]

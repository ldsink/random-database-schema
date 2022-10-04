from dataclasses import dataclass
from typing import List

from constants import ColumnDataType


@dataclass
class DatabaseItem:
    name: str
    comment: str = None


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

    def __post_init__(self):
        self.columns = sorted(self.columns, key=lambda _: (_.data_type, _.name))  # order by data_type

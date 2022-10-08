import random
from functools import cache
from typing import List

from constants import ColumnDataType
from models import DatabaseItem, TableColumnItem, TableItem
from modules.words import words
from modules.zen import zen_of_python


def get_random_word() -> str:
    return random.choice(words)


def get_database_item() -> DatabaseItem:
    return DatabaseItem(name=_get_random_name(), comment=_get_random_comment())


def get_table_column() -> TableColumnItem:
    return TableColumnItem(
        name=_get_random_name(),
        data_type=random.choice(_get_column_data_types()),
        null=random.choice([True, False]),
        comment=_get_random_comment()
    )


def get_table_item(database: DatabaseItem, column_size=200) -> TableItem:
    columns = []
    for i in range(column_size):
        columns.append(get_table_column())
    return TableItem(database=database, name=_get_random_name(), columns=columns, comment=_get_random_comment())


def _get_random_zen(max_len: int = 100) -> str:
    start = random.randint(0, len(zen_of_python) - 1)
    end = min(len(zen_of_python), start + random.randint(0, max_len))
    return zen_of_python[start:end]


def _get_random_name() -> str:
    return f"{get_random_word()}_{_get_random_zen()}"


def _get_random_comment() -> str:
    return _get_random_zen(200)


@cache
def _get_column_data_types() -> List[ColumnDataType]:
    return list(map(lambda c: c.value, ColumnDataType))

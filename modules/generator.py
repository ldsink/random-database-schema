import random
from functools import cache
from typing import List

from random_word import RandomWords

from constants import ColumnDataType
from models import DatabaseItem, TableColumnItem, TableItem

r = RandomWords()


def _get_random_name() -> str:
    words, word_num = [], random.randint(1, 5)
    for i in range(word_num):
        words.append(r.get_random_word())
    return "_".join(words)


def _get_random_comment() -> str:
    words, word_num = [], random.randint(0, 10)
    for i in range(word_num):
        words.append(r.get_random_word())
    return " ".join(words)


@cache
def _get_column_data_types() -> List[ColumnDataType]:
    return list(map(lambda c: c.value, ColumnDataType))


def get_database_item() -> DatabaseItem:
    return DatabaseItem(name=_get_random_name())


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
    return TableItem(database=database, name=_get_random_name(), columns=columns)

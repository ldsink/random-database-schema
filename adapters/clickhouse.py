from models import DatabaseItem, TableItem
from adapters.base import BaseAdapter


class ClickHouseAdapter(BaseAdapter):
    Adapter = "clickhouse"

    def __init__(self):
        pass

    def create_database(self, database: DatabaseItem):
        pass

    def create_table(self, table: TableItem):
        pass

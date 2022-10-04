from models import DatabaseItem, TableColumnItem, TableItem


class BaseAdapter:
    Adapter = None

    def __init__(self):
        pass

    def create_database(self, database: DatabaseItem):
        raise NotImplementedError

    def create_table(self, table: TableItem):
        raise NotImplementedError

    @classmethod
    def get_column_statement(cls, column: TableColumnItem) -> str:
        raise NotImplementedError

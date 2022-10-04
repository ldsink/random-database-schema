from models import DatabaseItem, TableItem


class BaseAdapter:
    Adapter = None

    def __init__(self):
        pass

    def create_database(self, database: DatabaseItem):
        raise NotImplementedError

    def create_table(self, table: TableItem):
        raise NotImplementedError

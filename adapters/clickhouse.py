import clickhouse_driver
from clickhouse_driver import defines

from adapters.base import BaseAdapter
from constants import ColumnDataType
from models import DatabaseItem, TableColumnItem, TableItem


class ClickHouseAdapter(BaseAdapter):
    Adapter = "clickhouse"

    # https://clickhouse.com/docs/en/sql-reference/data-types/
    _data_type_mapping = {
        ColumnDataType.INT: "INT",
        ColumnDataType.FLOAT: "FLOAT",
        ColumnDataType.STR: "String",
        ColumnDataType.BOOL: "Bool",
        ColumnDataType.DATE: "Date",
        ColumnDataType.DATETIME: "DateTime('Asia/Shanghai')",
    }

    def __init__(
            self, host="localhost", port=None,
            database=defines.DEFAULT_DATABASE,
            user=defines.DEFAULT_USER, password=defines.DEFAULT_PASSWORD
    ):
        self.client = clickhouse_driver.Client(host=host, port=port, database=database, user=user, password=password)

    def create_database(self, database: DatabaseItem):
        """
        https://clickhouse.com/docs/en/sql-reference/statements/create/database
        CREATE DATABASE [IF NOT EXISTS] db_name [ON CLUSTER cluster] [ENGINE = engine(...)] [COMMENT 'Comment']
        """
        query = f"CREATE DATABASE IF NOT EXISTS {database.name}"
        if database.comment:
            query = f"{query} COMMENT '{database.comment}'"
        self.client.execute(query)

    def create_table(self, table: TableItem):
        """https://clickhouse.com/docs/en/sql-reference/statements/create/table"""
        column_statements = list(map(self.get_column_statement, table.columns))
        primary_key = None
        for column in table.columns:
            if not column.null and column.data_type == ColumnDataType.DATE:
                primary_key = column.name
                break
        if not primary_key:
            primary_key = "auto_generated_primary_key"
            column = TableColumnItem(name=primary_key, data_type=ColumnDataType.DATE, null=False)
            column_statements.append(self.get_column_statement(column))
        column_statements.append(f"PRIMARY KEY({primary_key})")
        query = f"CREATE TABLE {table.database.name}.{table.name} ({', '.join(column_statements)}) ENGINE = MergeTree"
        if table.comment:
            query = f"{query} COMMENT '{table.comment}'"
        self.client.execute(query)

    @classmethod
    def get_column_statement(cls, column: TableColumnItem) -> str:
        s = f"{column.name} {cls._data_type_mapping[column.data_type]} {'' if column.null else 'NOT '}NULL"
        if column.default:
            s = f"{s} DEFAULT '{column.default}'"
        if column.comment:
            s = f"{s} COMMENT '{column.comment}'"
        return s

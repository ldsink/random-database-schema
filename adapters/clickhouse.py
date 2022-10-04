import clickhouse_driver
from clickhouse_driver import defines

from adapters.base import BaseAdapter
from models import DatabaseItem, TableItem


class ClickHouseAdapter(BaseAdapter):
    Adapter = "clickhouse"

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
        """
        https://clickhouse.com/docs/en/sql-reference/statements/create/table
        CREATE TABLE [IF NOT EXISTS] [db.]table_name [ON CLUSTER cluster]
(
    name1 [type1] [NULL|NOT NULL] [DEFAULT|MATERIALIZED|EPHEMERAL|ALIAS expr1] [compression_codec] [TTL expr1],
    name2 [type2] [NULL|NOT NULL] [DEFAULT|MATERIALIZED|EPHEMERAL|ALIAS expr2] [compression_codec] [TTL expr2],
    ...
) ENGINE = engine
        """

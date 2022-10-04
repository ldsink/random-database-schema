import tqdm

from adapters import get_adapter_cls
from modules.generator import get_database_item, get_table_item

if __name__ == '__main__':
    # TODO get args from shell
    database_num = 10000
    table_size = 200
    column_size = 200
    adapter = "clickhouse"
    kwargs = {}
    Adapter = get_adapter_cls(adapter)
    adapter = Adapter(**kwargs)

    for i in tqdm.tqdm(range(database_num)):
        database = get_database_item()
        adapter.create_database(database)
        for j in tqdm.tqdm(range(table_size)):
            table = get_table_item(database, column_size=column_size)
            adapter.create_table(table)

from .base import BaseAdapter
from .clickhouse import ClickHouseAdapter


def get_adapter_cls(adapter: str) -> BaseAdapter:
    for cls in [
        ClickHouseAdapter,
    ]:
        if cls.Adapter == adapter:
            return cls
    raise ValueError(f"Unsupported adapter: {adapter}")

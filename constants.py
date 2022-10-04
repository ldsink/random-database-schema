import enum


@enum.Enum
class ColumnDataType(enum.IntEnum):
    INT = enum.auto()
    FLOAT = enum.auto()
    STR = enum.auto()
    BOOL = enum.auto()
    DATE = enum.auto()
    DATETIME = enum.auto()

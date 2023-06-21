import pandas as pd
from typing import Iterable, TypeVar

T = TypeVar('T')
def magic_import(filename: str, cls: T) -> list[T]:
    df = pd.read_excel(filename)
    columns = list(cls.__annotations__.keys())
    data = [cls(**{col: row[i] for i, col in enumerate(columns)}) for _, row in df.iterrows()]
    return data

import pandas as pd
from dataclasses import dataclass
from magic import magic_import

@dataclass
class User:
    name: str
    age: int
    gender: str
    orders: int
    total: float

    def is_adult(self):
        return self.age >= 18
    
    def is_male(self):
        return self.gender == 'Male'

data = magic_import('data.xlsx', User)

print(data)

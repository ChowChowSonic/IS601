from calculator.AST import AST
from typing import List


class Calculations:
    history: List[AST] = []

    @classmethod
    def add_to_history(cls, item: AST):
        Calculations.history.append(item)

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def get_from_history(cls, num: int):
        return cls.history[num]

    @classmethod
    def clear_history(cls):
        cls.history.clear()

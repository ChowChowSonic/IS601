from AST import AST
from typing import List


class Calculator:
    history: List[AST] = []

    @staticmethod
    def add_to_history(cls, item: AST):
        cls.history.append(item)

    @staticmethod
    def get_history(cls):
        return cls.history

    @staticmethod
    def clear_history(cls):
        cls.history.clear()

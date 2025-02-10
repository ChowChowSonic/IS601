from AST import AST
from typing import List


class Calculations:
    history: List[AST] = []

    @staticmethod
    def add_to_history(item: AST):
        Calculations.history.append(item)

    @staticmethod
    def get_history():
        return Calculations.history

    @staticmethod
    def get_from_history(num: int):
        return Calculations.history[num]

    @staticmethod
    def clear_history():
        Calculations.history.clear()

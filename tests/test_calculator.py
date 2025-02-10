"""Tests the arg parsing capabilities of the calculator module."""

import pytest
from calculator import Calculator
from calculator.AST import (
    AdditionStmtAST,
    DivisionStmtAST,
    SubtractionStmtAST,
    MultiplicationStmtAST,
    NumberExprAST,
)
from calculator.calculations import Calculations


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 54),
        ("5", 5),
        ("10 +3", 13),
        ("10*3* 3", 90),
        ("10 / 3", 3.3333333333333335),
        ("100+5     ", 105),
        ("1+2+3", 6),
    ],
)
def test_calculator(test_input, expected):
    """Tests the printing function of the calculator"""
    assert Calculator.get_input(test_input) == expected
    with pytest.raises(ZeroDivisionError):
        assert Calculator.get_input("1/0") == 1

def test_history():
    """Tests the history functionality of the Calculations class"""
    Calculations.add_to_history(AdditionStmtAST(NumberExprAST(5), NumberExprAST(5)))
    Calculations.add_to_history(AdditionStmtAST(NumberExprAST(10), NumberExprAST(20)))
    Calculations.add_to_history(
        SubtractionStmtAST(NumberExprAST(10), NumberExprAST(20))
    )
    Calculations.add_to_history(
        MultiplicationStmtAST(NumberExprAST(10), NumberExprAST(2))
    )
    Calculations.add_to_history(DivisionStmtAST(NumberExprAST(10), NumberExprAST(20)))
    assert Calculations.get_from_history(0).codegen() == 10
    assert Calculations.get_from_history(1).codegen() == 30
    assert Calculations.get_from_history(2).codegen() == -10
    assert Calculations.get_from_history(3).codegen() == 20
    assert Calculations.get_from_history(4).codegen() == 0.5
    assert len(Calculations.get_history()) == 5
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

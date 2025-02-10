"""Tests the arg parsing capabilities of the calculator module."""

from calculator import parse_args, lower_operator_precidence, higher_operator_precidence
from calculator.AST import (
    AdditionStmtAST,
    DivisionStmtAST,
    SubtractionStmtAST,
    MultiplicationStmtAST,
    NumberExprAST,
)
from calculator.calculations import Calculations


def test_argparse():
    """Tests the arg parsing capabilities of the calculator module."""
    assert parse_args("1+2+3", "+4") == [1, "+", 2, "+", 3, "+", 4]
    assert parse_args("5-6*7/8") == [5, "-", 6, "*", 7, "/", 8]
    assert parse_args("9^10") == [9, "^", 10]


def test_calculation():
    """Tests the calculation function using long strings of input"""
    assert lower_operator_precidence(parse_args("2+3*4")).codegen() == 14
    assert lower_operator_precidence(parse_args("5-6*7/8")).codegen() == -0.25
    assert lower_operator_precidence(parse_args("9+10")).codegen() == 19
    assert higher_operator_precidence(parse_args("9*10")).codegen() == 90


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

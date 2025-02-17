"""Tests the arg parsing capabilities of the calculator modules."""

import pytest
from calculator import Calculator
from calculator.AST import (
    AdditionStmtAST,
    DivisionStmtAST,
    SubtractionStmtAST,
    MultiplicationStmtAST,
    NumberExprAST,
    AST,
)
from calculator.calculations import Calculations


def test_calculation(a, b, operation, expected):
    assert AST.create_AST_instance(a, b, operation).codegen() == expected


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

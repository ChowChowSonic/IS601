"""My Calculator Test"""

import pytest
from calculator.AST import (
    NumberExprAST,
    AdditionStmtAST,
    SubtractionStmtAST,
    MultiplicationStmtAST,
    DivisionStmtAST,
    AST,
    BinaryAST,
)


def test_ast():
    """Testing Abstract Syntax Tree"""
    # AST() & AST.codegen() throws an error when called
    with pytest.raises(NotImplementedError):
        AST()


def test_binaryast():
    """Test that the Binary AST class throws an error"""
    with pytest.raises(NotImplementedError):
        bast = BinaryAST(NumberExprAST(0), NumberExprAST(0))
        bast.codegen()


def test_addition():
    """Test that the addition function works"""
    assert AdditionStmtAST(NumberExprAST(2), NumberExprAST(2)).codegen() == 4


def test_subtraction():
    """Test that the subtraction function works"""
    assert SubtractionStmtAST(NumberExprAST(2), NumberExprAST(2)).codegen() == 0


def test_multiplication():
    """Test that the multiplication function works"""
    assert MultiplicationStmtAST(NumberExprAST(3), NumberExprAST(2)).codegen() == 6


def test_division():
    """Test that the division function works"""
    assert DivisionStmtAST(NumberExprAST(2), NumberExprAST(2)).codegen() == 1
    with pytest.raises(ZeroDivisionError):
        assert DivisionStmtAST(NumberExprAST(2), NumberExprAST(0)).codegen() == 1

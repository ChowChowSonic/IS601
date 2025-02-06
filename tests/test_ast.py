'''My Calculator Test'''
from calculator import AST

def test_addition():
    '''Test that the addition function works '''    
    assert AST.AdditionStmtAST(AST.NumberExprAST(2),AST.NumberExprAST(2)).codegen() == 4

def test_subtraction():
    '''Test that the subtraction function works '''    
    assert AST.SubtractionStmtAST(AST.NumberExprAST(2),AST.NumberExprAST(2)).codegen() == 0

def test_multiplication():
    '''Test that the multiplication function works '''    
    assert AST.MultiplicationStmtAST(AST.NumberExprAST(3),AST.NumberExprAST(2)).codegen() == 6

def test_division():
    '''Test that the division function works '''    
    assert AST.DivisionStmtAST(AST.NumberExprAST(2),AST.NumberExprAST(2)).codegen() == 1

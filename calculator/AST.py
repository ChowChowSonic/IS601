"""The base class & inherited classes for an Abstract Syntax tree"""
from __future__ import annotations 

class AST:
    """The base class class for an Abstract Syntax tree"""

    def __init__(self):
        """This shouldn't be legal, but I need a valid constructor to make pytest happy"""
        pass

    def codegen(self):
        raise NotImplementedError(
            "AST is an abstract class, AST.codegen() was not implemented!"
        )
    
    @staticmethod
    def create_AST_instance(
        lhs: 'AST' | int | float, rhs: 'AST' | int | float, operator: str
    ) -> 'AST':
        """Creates the actual AST based on the operator supplied"""
        possibilities = {
            "add": AdditionStmtAST,
            "+": AdditionStmtAST,
            "subtract": SubtractionStmtAST, 
            "-": SubtractionStmtAST,
            "multiply": MultiplicationStmtAST, 
            "*": MultiplicationStmtAST,
            "divide": DivisionStmtAST, 
            "/": DivisionStmtAST,
            "\\": DivisionStmtAST,
        }
        return possibilities[operator](lhs, rhs)


class BinaryAST(AST):

    def __init__(self, LHS: AST, RHS: AST):
        self.LHS: AST = LHS
        self.RHS: AST = RHS

    def codegen(self):
        raise NotImplementedError("BinaryAST does not implement a codegen function!")


class NumberExprAST(AST):
    """A class representing a number; 1234.5"""

    def __init__(self, HS):
        self.HS = HS

    def codegen(self):
        return self.HS


class AdditionStmtAST(BinaryAST):
    """A class representing an addition statement; a+b"""

    def codegen(self):
        return self.LHS.codegen() + self.RHS.codegen()


class SubtractionStmtAST(BinaryAST):
    """A class representing a subtraction statement; a-b"""

    def codegen(self):
        return self.LHS.codegen() - self.RHS.codegen()


class DivisionStmtAST(BinaryAST):
    """A class representing a division statement; a/b"""

    def codegen(self):
        r = self.RHS.codegen()
        if r == 0:
            raise ZeroDivisionError("Divide by 0 error!")
        return self.LHS.codegen() / r


class MultiplicationStmtAST(BinaryAST):
    """A class representing a multiplication statement; a*b"""

    def codegen(self):
        return self.LHS.codegen() * self.RHS.codegen()

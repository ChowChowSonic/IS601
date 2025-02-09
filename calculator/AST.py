"""The base class & inherited classes for an Abstract Syntax tree"""


class AST:
    """The base class class for an Abstract Syntax tree"""

    def __init__(self):
        raise NotImplementedError("AST is an abstract class, AST() is not callable!")

    def codegen():
        raise NotImplementedError(
            "AST is an abstract class, AST.codegen() was not implemented!"
        )


class BinaryAST(AST):

    def __init__(self, LHS: AST, RHS: AST):
        self.LHS:AST = LHS
        self.RHS:AST = RHS

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

"""The base class & inherited classes for an Abstract Syntax tree"""


class AST:
    """The base class class for an Abstract Syntax tree"""

    def codegen():
        raise NotImplementedError(
            "AST is an abstract class, AST.codegen() was not implemented!"
        )


class NumberExprAST(AST):
    """A class representing a number; 1234.5"""

    def __init__(self, HS):
        self.HS = HS

    def codegen(self):
        return self.HS


class AdditionStmtAST(AST):
    """A class representing an addition statement; a+b"""

    def __init__(self, LHS, RHS):
        self.LHS = LHS
        self.RHS = RHS

    def codegen(self):
        return self.LHS.codegen() + self.RHS.codegen()


class SubtractionStmtAST(AST):
    """A class representing a subtraction statement; a-b"""

    def __init__(self, LHS, RHS):
        self.LHS = LHS
        self.RHS = RHS

    def codegen(self):
        return self.LHS.codegen() - self.RHS.codegen()


class DivisionStmtAST(AST):
    """A class representing a division statement; a/b"""

    def __init__(self, LHS, RHS):
        self.LHS = LHS
        self.RHS = RHS

    def codegen(self):
        r = self.RHS.codegen()
        if r == 0:
            raise Exception("Divide by 0 error!")
        return self.LHS.codegen() / self.RHS.codegen()


class MultiplicationStmtAST(AST):
    """A class representing a multiplication statement; a*b"""

    def __init__(self, LHS, RHS):
        self.LHS = LHS
        self.RHS = RHS

    def codegen(self):
        return self.LHS.codegen() * self.RHS.codegen()

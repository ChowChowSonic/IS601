"""The base class & inherited classes for an Abstract Syntax tree"""


class AST:
    """The base class class for an Abstract Syntax tree"""

    def codegen():
        raise NotImplementedError(
            "AST is an abstract class, AST.codegen() was not implemented!"
        )

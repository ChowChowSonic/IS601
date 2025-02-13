from tokenizer import Tokenizer
from calculations import Calculations
from AST import AST, NumberExprAST, AdditionStmtAST, SubtractionStmtAST, MultiplicationStmtAST, DivisionStmtAST

import sys


class Calculator:
    @staticmethod
    def _parse_args(*args: str) -> list[int | float | str]:
        """parses any number of strings as one long string, then tokenizes it into an array"""
        content = "".join(map(str, args))
        tokenizer = Tokenizer(content)
        arr = []
        while tokenizer.has_next():
            token = tokenizer.get_token()
            arr.append(token)
        return arr

    # Ok so if I want to implement a recusive descent parser, I can do one of two things:
    # Either:
    #   A: Repeat myself a little bit with the AST-parsing functions
    #       or
    #   B: Don't repeat myself, but use roughly 6 if-stmts in one recursive function
    # Lord help me. 

    @staticmethod
    def _higher_operator_precidence(tokens: list[int | float | str]) -> AST:
        lhs = NumberExprAST(tokens.pop(0))
        while len(tokens) > 0 and isinstance(tokens[0], str) and tokens[0] in "*/\\":
            op = tokens.pop(0)
            lhs = AST.AST.create_AST_instance(lhs, NumberExprAST(tokens.pop(0)), op)
        return lhs

    @staticmethod
    def _lower_operator_precidence(tokens: list[int | float | str]) -> AST:
        lhs = Calculator._higher_operator_precidence(tokens)
        while len(tokens) > 0 and isinstance(tokens[0], str) and tokens[0] in "+-":
            op = tokens.pop(0)
            lhs = AST.AST.create_AST_instance(
                lhs, Calculator._higher_operator_precidence(tokens), op
            )
        return lhs

    # Attempt #1 to not repeat myself
    # def generate_AST(tokens:list[int|float|str], operators:list[str]) -> AST:
    #     '''generates an AST from an array of tokens; I tried not to repeat myself and dear Lord this turned out to be a mess'''
    #     lhs = generate_AST(tokens, operators[1:]) if len(operators) == 1 else NumberExprAST(tokens.pop(0))
    #     if tokens[0] not in operators[0]:
    #         return lhs
    #     x=tokens.pop(0)
    #     rhs = generate_AST(tokens, operators[1:]) if len(operators) == 1 else NumberExprAST(tokens.pop(0))
    #     possibilities={'+':AdditionStmtAST, '-':SubtractionStmtAST, '*':MultiplicationStmtAST, '/':DivisionStmtAST, '\\':DivisionStmtAST}
    #     return possibilities[x](lhs, rhs)

    @staticmethod
    def _print_result(*args: list[str]) -> int | float:
        """Prints the result of a mathematical calculation passed via 1 or more argument(s)"""
        tokens = Calculator._parse_args(*args)
        ast = Calculator._lower_operator_precidence(tokens)
        result = ast.codegen()
        print(result)
        Calculations.add_to_history(ast)
        return result

    @staticmethod
    def get_input(argv: list[str]) -> float | int:
        # if len(argv) == 1:
        #     ctr = 0
        #     x = " "
        #     while x != "":
        #         try:
        #             x = input("!" + str(ctr) + ": ")
        #         except EOFError:
        #             # Useful for when we pipe something as input rather than manually inputtng something
        #             break
        #         ctr += 1
        #         if x != "":
        #             Calculator._print_result(x)
        # else:
        return Calculator._print_result(*argv)

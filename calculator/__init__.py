from tokenizer import Tokenizer
from calculations import Calculations
from AST import *

def parse_args(*args):
    '''parses any number of strings as one long string, then tokenizes it into an array'''
    content = "".join(map(str, args))
    tokenizer = Tokenizer(content)
    arr=[]
    while tokenizer.has_next():
        token = tokenizer.get_token()
        if token == "":
            break
        arr.append(token)
    return arr

# Ok so if I want to implement a recusive descent parser, I can do one of two things: 
# Either: 
#   A: Repeat myself a little bit with the AST-parsing functions
#       or
#   B: Don't repeat myself, but use roughly 6 if-stmts in one recursive function
# Lord help me.  
    
def create_AST_instance(lhs:AST|int|float, rhs:AST|int|float, operator:str) -> AST:
     possibilities={'+':AdditionStmtAST, '-':SubtractionStmtAST, '*':MultiplicationStmtAST, '/':DivisionStmtAST, '\\':DivisionStmtAST}
     return possibilities[operator](lhs, rhs)

def higher_operator_precidence(tokens:list[int|float|str]):
    lhs = NumberExprAST(tokens.pop(0))
    while len(tokens) > 0 and isinstance(tokens[0], str) and tokens[0] in '*/\\': 
        op=tokens.pop(0)
        lhs = create_AST_instance(lhs, NumberExprAST(tokens.pop(0)), op)
    return lhs 

def lower_operator_precidence(tokens:list[int|float|str])-> AST:
    lhs = higher_operator_precidence(tokens)
    while len(tokens) > 0 and isinstance(tokens[0], str) and tokens[0] in '+-': 
        op = tokens.pop(0)
        lhs = create_AST_instance(lhs, higher_operator_precidence(tokens), op)
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


if __name__ == "__main__":
    tokens = parse_args(*sys.argv[1:])
	
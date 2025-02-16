import Faker 
import pytest 

from calculator.AST import (
	AST, 
	NumberExprAST, 
	AdditionStmtAST, 
	SubtractionStmtAST,
	MultiplicationStmtAST,
	DivisionStmtAST, 
)


def _add(a:int|float,b:int|float):
	return a+b 

def _sub(a:int|float,b:int|float):
	return a-b

def _mul(a:int|float,b:int|float): 
	return a*b

def _div(a:int|float,b:int|float): 
	if b == 0:
		return "ZeroDivisionError"
	return a/b 

faker=Faker()

def generate_test_data(len_data): 
	ops={
		'+':_add,
		'-':_sub, 
		'*':_mul, 
		'/':_div
	}
	
	for i in range(len_data): 
		a = NumberExprAST(faker.random_number(digits=2))
		b = NumberExprAST(faker.random_number(digits=2))
		op = faker.random_element(elements=ops.keys()) 
		expected = ops[op](a.codegen(),b.codegen())

		yield a,b,op,expected

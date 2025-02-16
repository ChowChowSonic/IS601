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

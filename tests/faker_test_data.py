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


def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
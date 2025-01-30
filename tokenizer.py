import re 
def getNumConst(string):
	return int(string)
def getOperator(string):
	return string[0]
def getToken(string):
	functions = {} 
	functions['+']=getOperator
	functions['-']=getOperator
	functions['*']=getOperator
	functions['/']=getOperator
	functions['\\']=getOperator
	for i in range(ord('0'), ord('9')):
		functions[chr(i)]=getNumConst
	return functions[string[0]](string)
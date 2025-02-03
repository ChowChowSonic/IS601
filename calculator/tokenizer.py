import re 
class tokenizer:
	def __init__(self, content):
		self.index = 0
		self.content = content.strip()
	def getNumConst(self):
		ret=""
		while self.index<len(self.content) and self.content[self.index] in "1234567890":
			ret+=self.content[self.index]
			self.index+=1
		return int(ret)
	def getOperator(self):
		self.index+=1
		return self.content[self.index-1]
	def getToken(self):
		if self.index >= len(self.content):
			return ''
		functions = {} 
		functions['+']=self.getOperator
		functions['-']=self.getOperator
		functions['*']=self.getOperator
		functions['/']=self.getOperator
		functions['\\']=self.getOperator
		for i in range(ord('0'), ord('9')):
			functions[chr(i)]=self.getNumConst
		while self.content[self.index] in " \t\n":
			self.index+=1
		return functions[self.content[self.index]]()
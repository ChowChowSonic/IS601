from app.commands import Command
class multiply(Command):
	def __init__(self, a, b):
		self.a = a
		self.b = b 

	def execute(self):
		print("The result of",self.a,"multiply",self.b,"is equal to",self.a+self.b) 
from app.commands import Command
class divide(Command):
	def __init__(self, a, b):
		self.a = a
		self.b = b 

	def execute(self):
		print("The result of",self.a,"divide",self.b,"is equal to",self.a+self.b)
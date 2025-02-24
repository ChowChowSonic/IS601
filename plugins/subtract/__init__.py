from app.commands import Command
class subtract(Command):
	def __init__(self, a, b):
		self.a = a
		self.b = b 

	def execute(self):
		print("The result of",self.a,"subtract",self.b,"is equal to",self.a+self.b) 
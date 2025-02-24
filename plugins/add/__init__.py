from app.commands import Command
class add(Command):
	def __init__(self, a, b):
		self.a = a
		self.b = b 

	def execute(self):
		print("The result of",self.a,"add",self.b,"is equal to",self.a+self.b) 
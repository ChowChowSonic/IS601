from app.commands import Command
from multiprocessing import Process
class divide(Command):
	def __init__(self):
		pass 
	def execute(self, args:list[str]):
		print("The result of",args[0],"divide",args[1],"is equal to",int(args[0])//int(args[1])) 
		# p.start()
		# p.join()
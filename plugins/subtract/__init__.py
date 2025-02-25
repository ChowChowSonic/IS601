from app.commands import Command
from multiprocessing import Process 
class subtract(Command):
	def __init__(self):
		pass 
	def execute(self, args:list[str]):
		p=Process(target=print,args=("The result of",args[0],"subtract",args[1],"is equal to",int(args[0])-int(args[1])))
		p.start()
		p.join()
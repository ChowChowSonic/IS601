

class Command: 
	def __init__(self):
		pass

	def execute(self, args:list[str]):
		raise NotImplementedError("Command is an abstract class!")

class CommandHandler: 

	def __init__(self):
		self.commands = {}


	def register_command(self, name: str, cmd: Command):
			self.commands[name]=cmd

	def execute_command(self, name:str, args:list[str]): 
			try:
				self.commands[name].execute(args) 
			except KeyError: 
				print(f"No suh command: {name}")
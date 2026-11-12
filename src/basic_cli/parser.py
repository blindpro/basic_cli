from . import command
class parser():
    def __init__(self):
        self.commands = {}
    def add_command(self,name,action,help_text = ""):
        self.commands[name] = command(input,action,help_text)
    def parse(self,input):
        if input not in commands:
            print("invalid command")
        else:
            to_run = commands[input]
            to_run.run()
    
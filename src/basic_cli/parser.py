from sys import exit
from .command import command
from  . import text_manager as text
class parser():
    def __init__(self,name):
        self.commands = {}
        self.name = name
    def add_command(self,name,action,help_text = ""):
        self.commands[name] = command(input,action,help_text)
    def parse(self,input):
        input = str(input)
        base = text.get_base(input)
        if base == self.name:
            print(f"{name}, type {name} help for usage")
        elif base == "exit" or input == "quit":
            sys.exit()
        elif base == help:
            help()
            return
        elif base not in self.commands:
            print("invalid command")
        else:
            to_run = self.commands[base]
            to_run.run()
    def help(self):
        print("usage")
        for key,value in self.commands.items():
            print(key)
            print(value.help_text)
            
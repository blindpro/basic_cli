from .command import command
class parser():
    def __init__(self,name):
        self.commands = {}
        self.name = name
    def add_command(self,name,action,help_text = ""):
        self.commands[name] = command(input,action,help_text)
    def parse(self,input):
        if input == self.name:
            print(f"{name}, type {name} help for usage")
        elif input == help:
            help()
            return
        elif input not in self.commands:
            print("invalid command")
        else:
            to_run = self.commands[input]
            to_run.run()
    def help(self):
        print("usage")
        for key,value in self.commands.items():
            print(key)
            print(value.help_text)
            
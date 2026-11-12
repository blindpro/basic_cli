class parser():
    def __init__(self):
        self.commands = {}
    def add_command(self,name,action):
        self.commands[name] = action
    def parse(self,input):
        if input not in commands:
            print("invalid command")
        else:
            action = commands[input]
            action()
    
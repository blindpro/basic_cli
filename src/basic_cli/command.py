class command():
    def __init__(self,name,action,help_text):
        self.name = name
        self.action = action
        self.help_text = help_text
    def run(self):
        action()
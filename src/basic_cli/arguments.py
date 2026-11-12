from.text_manager import get_flags, get_options
class arguments():
    def __init__(self,text):
        self.text = text
        self.options = get_options(text)
        self.flags = get_flags(text)
    def has_option(self,option):
        return option in self.options
    def has_flag(self,flag):
        return flag in self.flags
    
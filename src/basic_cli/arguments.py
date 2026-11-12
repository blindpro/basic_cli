from.text_manager import get_flags, get_options
class arguments():
    def __init__(self,text):
        self.text = text
        self.options = get_options(text)
        self.flags = get_flags(text)
    def has_option(self,option):
        new_option = option
        if option.startswith("-") == False:
            new_option = f"-{option}"
        return new_option in self.options
    def has_flag(self,flag):
        new_flag = flag
        if flag.startswith("--") == False:
            new_flag = f"--{flag}"
        return new_flag in self.flags
    
def get_base(text):
    parts = text.split(" ")
    return parts[0]
def get_options(text):
    options = []
    parts = text.split(" ")
    for item in parts:
        if item.startswith("-") and item.count("-") == 1:
            options.append(item)
    return options
def get_flags(text):
    flags = []
    parts = text.split(" ")
    for item in parts:
        if item.startswith("--") and item.count("-") == 2:
            flags.append(item)
    return flags
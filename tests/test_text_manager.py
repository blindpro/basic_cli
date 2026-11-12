from basic_cli import text_manager as text
def test_get_base():
    output = text.get_base("base arg arg --flag")
    assert output == "base"
def test_options():
    options = text.get_options("base -option1 -option2 --flag")
    assert len(options) == 2
def test_flags():
    flags = text.get_flags("base -option -another_option --f --flag --third_flag")
    assert len(flags) == 3
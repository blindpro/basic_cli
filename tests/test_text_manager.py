from basic_cli import text_manager as text
def test_get_base():
    output = text.get_base("base arg arg --flag")
    assert output == "base"
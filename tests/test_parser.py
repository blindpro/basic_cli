from basic_cli.parser import parser
p = parser("tester")
def test_invalid(capsys):
    p.parse("this is invalid")
    captured = capsys.readouterr()
    assert captured.out == "invalid command\n"
def test_random(capsys):
    p.parse(26)
    captured = capsys.readouterr()
    assert captured.out == "invalid command\n"
def greet(args):
    print("hi!")
p.add_command("greet",greet,"Greets.")
def test_command_runner(capsys):
    p.parse("greet")
    captured = capsys.readouterr()
    assert captured.out == "hi!\n"

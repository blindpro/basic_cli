from basic_cli.arguments import arguments
def test_options():
    args = arguments("base -option --flag")
    assert args.has_option("-option") == True
def test_flags():
    args = arguments("base -option --flag")
    assert args.has_flag("--flag") == True
def test_auto_dash_option():
    args = arguments("base -option --flag")
    assert args.has_option("option") == True
def test_auto_dash_flag():
    args = arguments("base -option --flag")
    assert args.has_flag("flag") == True
import pytest

from am_i_even_or_odd.cli import main


def test_cli_even_plain(capsys):
    exit_code = main(["4"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "even"


def test_cli_odd_plain(capsys):
    exit_code = main(["7"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "odd"


def test_cli_negative_number(capsys):
    exit_code = main(["-4"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "even"


def test_cli_fun_mode_mentions_number(capsys):
    exit_code = main(["4", "--fun"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "4" in captured.out
    # Fun mode should say more than just "even"
    assert captured.out.strip() != "even"


def test_cli_fun_mode_odd(capsys):
    exit_code = main(["7", "--fun"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "7" in captured.out
    assert captured.out.strip() != "odd"


def test_cli_invalid_input_exits_nonzero(capsys):
    exit_code = main(["not-a-number"])
    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.err  # argparse prints its usage/error to stderr


def test_cli_no_args_exits_nonzero(capsys):
    exit_code = main([])
    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.err

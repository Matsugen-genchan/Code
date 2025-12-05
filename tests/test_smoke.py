"""Basic smoke tests for the MedNote CLI."""
from mednote import cli


def test_build_parser_produces_help(capsys):
    parser = cli.build_parser()
    parser.print_help()
    captured = capsys.readouterr()
    assert "mednote" in captured.out
    assert "Manage personal medical notes" in captured.out

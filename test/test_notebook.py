import pytest
from notebook import notebook

def test_convert(capsys):
    """Correct my_name argument prints"""
    notebook.convert("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out



import sys
import pytest
from argparse import ArgumentTypeError

from app.parser import parse
from app.models import Arguments

def test_parser_with_all_args(monkeypatch):
    test_args = ['main.py', '--file=data.csv', '--where=Price>100', '--aggregate=Price=avg']
    monkeypatch.setattr(sys, 'argv', test_args)

    result = parse()
    assert isinstance(result, Arguments)
    assert result.file == 'data.csv'
    assert result.where == 'Price>100'
    assert result.aggregate == 'Price=avg'


def test_parser_with_required_only(monkeypatch):
    test_args = ['main.py', '--file=data.csv']
    monkeypatch.setattr(sys, 'argv', test_args)

    result = parse()
    assert result.file == 'data.csv'
    assert result.where is None
    assert result.aggregate is None


def test_parser_raises_without_file(monkeypatch):
    test_args = ['main.py', '--where=Price>100']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(ArgumentTypeError, match="filename can`t be empty"):
        parse()
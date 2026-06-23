from importlib import import_module


TextBase = import_module("나의_패키지.core").TextBase


def test_tokenize():
    base = TextBase("Python package test")

    assert base._tokenize() == ["Python", "package", "test"]


def test_char_tokenize():
    base = TextBase("ab cd")

    assert base.char_tokenize() == ["a", "b", "c", "d"]

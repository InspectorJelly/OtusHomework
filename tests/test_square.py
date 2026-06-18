from src.figure import Figure
from src.rectangle import Rectangle
from src.square import Square
import pytest


def test_create_square():
    s = Square(4)
    assert s.side_a == 4


def test_impossible_square():
    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Square(-3)

    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Square(0)


def test_square_area():
    s = Square(4)
    assert s.area == 16


def test_square_perimeter():
    s = Square(4)
    assert s.perimeter == 16

from src.figure import Figure
from src.rectangle import Rectangle
import pytest

def test_create_rectangle():
    r = Rectangle(3, 5)
    assert r.side_a == 3
    assert r.side_b == 5


def test_impossible_rectangle():
    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Rectangle(3, -5)

    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Rectangle(-3, 5)

    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Rectangle(3, 0)


def test_rectangle_area():
    r = Rectangle(3, 5)
    assert r.area == 15


def test_rectangle_perimeter():
    r = Rectangle(3, 5)
    assert r.perimeter == 16

from src.figure import Figure
from src.triangle import Triangle
import pytest


def test_create_triangle():
    t =Triangle(3, 4, 5)
    assert t.side_a == 3
    assert t.side_b == 4
    assert t.side_c == 5


def test_impossible_triangle1():
    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Triangle(-3, 4, 5)

    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Triangle(3, -4, 5)

    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Triangle(3, 4, -5)

    with pytest.raises(ValueError, match="Стороны фигуры должны быть положительными числами"):
        Triangle(0, 4, 5)


def test_impossible_triangle2():
    with pytest.raises(ValueError, match="Треугольник с такими сторонами не существует"):
        Triangle(10, 4, 5)

    with pytest.raises(ValueError, match="Треугольник с такими сторонами не существует"):
        Triangle(3, 10, 5)

    with pytest.raises(ValueError, match="Треугольник с такими сторонами не существует"):
        Triangle(3, 4, 10)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert t.area == 6.0


def test_triangle_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter == 12

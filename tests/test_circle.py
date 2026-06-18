from src.figure import Figure
from src.circle import Circle
import pytest


def test_create_circle():
    c = Circle(5)
    assert c.radius == 5

def test_impossible_circle():
    with pytest.raises(ValueError, match="Радиус круга должен быть положительными числом"):
        Circle(-5)

    with pytest.raises(ValueError, match="Радиус круга должен быть положительными числом"):
        Circle(0)


def test_circle_area():
    c = Circle(5)
    assert c.area == 78.54


def test_circle_perimeter():
    c = Circle(5)
    assert c.perimeter == 31.42

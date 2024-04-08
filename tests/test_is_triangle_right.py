import pytest
from main import SchoolGeometryCalculator as Calc


class TestIsTriangleRight:
    @staticmethod
    def test_right_triangle():
        # Test a right-angled triangle
        assert Calc.is_triangle_right(3, 4, 5) is True

    @staticmethod
    def test_not_right_triangle():
        # Test a triangle that is not right-angled
        assert Calc.is_triangle_right(3, 4, 6) is False

    @staticmethod
    def test_invalid_triangle():
        # Test sides that do not form a triangle
        with pytest.raises(ValueError):
            Calc.is_triangle_right(1, 2, 10)

    @staticmethod
    def test_negative_sides():
        # Test negative side lengths
        with pytest.raises(ValueError):
            Calc.is_triangle_right(-3, 4, 5)

    @staticmethod
    def test_zero_length_sides():
        # Test zero length sides
        with pytest.raises(ValueError):
            Calc.is_triangle_right(0, 4, 5)



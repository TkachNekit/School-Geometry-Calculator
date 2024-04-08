import math
import pytest
from main import SchoolGeometryCalculator as Calc


class TestGeometryCalculator:
    @staticmethod
    @pytest.mark.parametrize("a, b, c, expected_area", [
        (3, 4, 5, 6),               # Valid sides (3-4-5 triangle)
        (5.5, 6.5, 7.5, 17.407231794573196),  # Valid sides with floats
        (2, 2, 2, math.sqrt(3)),   # Equilateral triangle
        (5, 5, 6, 12),              # Isosceles triangle
        (3, 4, 6, 5.33268225)       # Scalene triangle
    ])
    def test_triangle_area_valid(a, b, c, expected_area):
        assert math.isclose(Calc.triangle_area(a, b, c), expected_area, rel_tol=1e-9)

    @staticmethod
    @pytest.mark.parametrize("a, b, c", [
        (-1, 2, 3),                 # Negative side
        (0, 2, 3),                  # Zero side
        (1, 2, 4),                  # Invalid triangle (sum of two sides is less than the third side)
    ])
    def test_triangle_area_invalid(a, b, c):
        with pytest.raises(ValueError):
            Calc.triangle_area(a, b, c)
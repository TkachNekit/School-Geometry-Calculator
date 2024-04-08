# School Geometry Calculator

---

This project provides a Python class `SchoolGeometryCalculator` for performing geometric calculations. 
It supports the calculation of the area of a circle and the area of a triangle.

## Usage

---
Here's how you can use the `SchoolGeometryCalculator` class:
```python
from geometry_calculator import SchoolGeometryCalculator

# Create an instance of the class
calculator = SchoolGeometryCalculator()

# Calculate the area of a circle
radius = 5
circle_area = calculator.circle_area(radius)
print("Area of a circle with radius", radius, ":", circle_area)

# Calculate the area of a triangle
side1 = 3
side2 = 4
side3 = 5
triangle_area = calculator.triangle_area(side1, side2, side3)
print("Area of a triangle with sides", side1, ",", side2, ",", side3, ":", triangle_area)

# Check if a triangle is right-angled
is_right_triangle = calculator.is_triangle_right(side1, side2, side3)
print("Is the triangle right-angled?", is_right_triangle)
```

## Methods
### `circle_area(radius: float) -> float`
_Calculates the area of a circle given its radius._
- radius: Circle radius.
- Returns: Circle area.

### `triangle_area(a: float, b: float, c: float) -> float`
_Calculates the area of a triangle given the lengths of its three sides._
- a: Length of the first side.
- b: Length of the second side.
- c: Length of the third side.
- Returns: Triangle area.
### `is_triangle_right(a: float, b: float, c: float) -> bool`
_Checks if a triangle is right-angled based on the lengths of its sides._
- a: Length of the first side.
- b: Length of the second side.
- c: Length of the third side.
- Returns: True if the triangle is right-angled, False otherwise.

### Installation
```text
pip install school-geometry-calculator
```

### Licence
This project is licensed under the TKACH License - see the LICENSE file for details.
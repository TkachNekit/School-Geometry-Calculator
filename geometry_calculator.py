import math


class SchoolGeometryCalculator:
    """
    Class for geometric calculators.

    Supported shapes:
    - Circle
    - Triangle

    Example usage:
    ```
    python
        # Create an instance of the class
        calculator = GeometryCalculator()

        # Calculate the area of a circle
        radius = 5
        circle_area = calculator.calculate_circle_area(radius)
        print("Area of a circle with radius", radius, ":", circle_area)

        # Calculate the area of a triangle
        side1 = 3
        side2 = 4
        side3 = 5
        triangle_area = calculator.calculate_triangle_area(side1, side2, side3)
        print("Area of a triangle with sides", side1, ",", side2, ",", side3, ":", triangle_area)
    ```
    """

    @staticmethod
    def circle_area(radius: float) -> float:
        """
        Calculates circle area by given radius.

        :param radius: Circle radius.
        :type radius: float
        :return: Circle area.
        :rtype: float
        """

        if radius < 0:
            raise ValueError("Radius can't be < 0")

        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(a: float, b: float, c: float) -> float:
        """
        Calculates triangle area by given 3 sides.

        :param a: First side length.
        :type a: float
        :param b: Second side length.
        :type b: float
        :param c: Third side length.
        :type c: float
        :return: Triangle area.
        :rtype: float
        """
        triangle = [a, b, c]
        if any(side <= 0 for side in triangle) or (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Side's length has to be > 0")

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Sides cannot form a triangle")

        p = (a + b + c) / 2
        # Heron's formula
        triangle_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return triangle_area

    @staticmethod
    def is_triangle_right(a: float, b: float, c: float) -> bool:
        """
        Checks if a triangle is a right triangle based on its side lengths.

        Arguments:
        - side1 (float): Length of the first side.
        - side2 (float): Length of the second side.
        - side3 (float): Length of the third side.

        Returns:
        - is_right (bool): True if the triangle is right-angled, False otherwise.
        """
        triangle = [a, b, c]
        if any(side <= 0 for side in triangle):
            raise ValueError("Triangle side's length has to be > 0")

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Sides cannot form a triangle")

        sides = sorted([a, b, c])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

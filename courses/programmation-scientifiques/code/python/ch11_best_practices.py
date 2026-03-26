"""
Chapter 11: Best Practices — Testing, Documentation, Git
"""
import math


def quadratic_roots(a, b, c):
    """
    Solve the quadratic equation ax² + bx + c = 0.

    Parameters
    ----------
    a : float
        Coefficient of x².
    b : float
        Coefficient of x.
    c : float
        Constant term.

    Returns
    -------
    tuple of float or None
        The two roots, or (None, None) if no real roots.

    Examples
    --------
    >>> quadratic_roots(1, -5, 6)
    (3.0, 2.0)
    >>> quadratic_roots(1, 0, 1)
    (None, None)
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2


# === Testing with assert ===
def test_quadratic_roots():
    """Test the quadratic_roots function."""
    # x² - 5x + 6 = 0 → x = 3, x = 2
    x1, x2 = quadratic_roots(1, -5, 6)
    assert abs(x1 - 3.0) < 1e-10, f"Expected 3.0, got {x1}"
    assert abs(x2 - 2.0) < 1e-10, f"Expected 2.0, got {x2}"

    # x² + 1 = 0 → no real roots
    x1, x2 = quadratic_roots(1, 0, 1)
    assert x1 is None and x2 is None

    # x² - 4 = 0 → x = 2, x = -2
    x1, x2 = quadratic_roots(1, 0, -4)
    assert abs(x1 - 2.0) < 1e-10
    assert abs(x2 + 2.0) < 1e-10

    print("All tests passed!")


if __name__ == "__main__":
    test_quadratic_roots()

    # PEP 8 naming conventions
    MAX_ITERATIONS = 100       # constant
    student_count = 42         # variable
    def calculate_mean(data):  # function
        return sum(data) / len(data)

    print(f"Mean of [1,2,3,4,5]: {calculate_mean([1,2,3,4,5])}")

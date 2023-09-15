from functions.level_2.two_square_equation import solve_square_equation
import random


def test__solve_square_equation__negative_discriminant():
    assert solve_square_equation(0.2, 0.2, 0.2) == (None, None)


def test__solve_square_equation__no_coefficients():
    assert solve_square_equation(0, 0, 0.2) == (None, None)


def test__solve_square_equation__no_square_coefficient_positive_const():
    assert solve_square_equation(0, 1, 0.2) == (-0.2, None)


def test__solve_square_equation__no_square_coefficient_negative_const():
    assert solve_square_equation(0, 1, -0.2) == (0.2, None)


def test__solve_square_equation__positive_coefficients():
    assert solve_square_equation(2,5,2) == (-2.0, -0.5)


def test__solve_square_equation__positive_random_coefficients():
    square, linear, const = (
            round(random.uniform(1.0, 1.5), 2),
            round(random.uniform(3.0, 4.0), 2),
            round(random.uniform(1.0, 1.5), 2)
        )
    result = solve_square_equation(
        round(random.uniform(1.0, 1.5), 2),
        round(random.uniform(3.0, 4.0), 2),
        round(random.uniform(1.0, 1.5), 2)
    )
    assert result[0] is not None and result[1] is not None

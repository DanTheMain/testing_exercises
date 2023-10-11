from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__return_none_with_negative_discriminant():
    assert solve_square_equation(0.2, 0.2, 0.2) == (None, None)


def test__solve_square_equation__return_none_with_no_coefficients():
    assert solve_square_equation(0, 0, 0.2) == (None, None)


def test__solve_square_equation__no_square_coefficient_positive_const():
    assert solve_square_equation(0, 1, 0.2) == (-0.2, None)


def test__solve_square_equation__no_square_coefficient_negative_const():
    assert solve_square_equation(0, 1, -0.2) == (0.2, None)


def test__solve_square_equation__positive_coefficients():
    assert solve_square_equation(2, 5, 2) == (-2.0, -0.5)


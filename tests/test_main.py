"""Testing the main driver code """

import pytest
from main import calculate_and_print


# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize(
    "a_string, b_string, operation_string, expected_string",
    [
        ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
        ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
        ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
        ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
        (
            "1",
            "0",
            "divide",
            "An error occurred: Cannot divide by zero",
        ),  # Adjusted for the actual error message
        (
            "9",
            "3",
            "unknown",
            "Unknown operation: unknown",
        ),  # Test for unknown operation
        (
            "a",
            "3",
            "add",
            "Invalid number input: a or 3 is not a valid number.",
        ),  # Testing invalid number input
        (
            "5",
            "b",
            "subtract",
            "Invalid number input: 5 or b is not a valid number.",
        ),  # Testing another invalid number input
    ],
)
def test_calculate_and_print(
    a_string, b_string, operation_string, expected_string, capsys
):
    """Test's the main calculate & print class"""
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string


def test_div_by_0(capsys):
    """Tests that dividing by 0 throws the expected error"""
    calculate_and_print("1", "0", "divide")
    captured = capsys.readouterr()
    assert captured.out.strip() == "An error occurred: Cannot divide by zero"


# def test_from_pipe():
#     oldstdin = sys.stdin
#     sys.stdin = open("testdata.txt")
#     assert calculate_and_print() is None
#     sys.stdin = oldstdin

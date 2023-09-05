import pytest

from rpncalc.rpn_v2 import RPNCalculator
from rpncalc.utils import Config

# rpncalc/test_rpn_v2.py

@pytest.fixture
def rpn() -> RPNCalculator:
    """A RPN Calculator with a default config"""
    return RPNCalculator(Config())


def test_complex_example():
    rpn = RPNCalculator(Config())

    rpn.evaluate("1")
    assert rpn.stack == [1]
    rpn.evaluate("2")
    assert rpn.stack == [1, 2]
    rpn.evaluate("+")
    assert rpn.stack == [3]
    rpn.evaluate("5")
    assert rpn.stack == [3, 5]
    rpn.evaluate("*")
    assert rpn.stack == [15]


def test_stack_push():
    rpn = RPNCalculator(Config())
    rpn.evaluate("1")
    rpn.evaluate("2")
    assert rpn.stack == [1, 2]

@pytest.mark.parametrize("op, expected", [
    ("+", 3), ("-", -1), ("*", 2), ("/", 0.5),
])
def test_operations(op, expected):
    rpn = RPNCalculator(Config())
    rpn.stack = [1, 2]
    rpn.evaluate(op)
    assert rpn.stack == [expected]


@pytest.mark.parametrize(
    "n", [1.5, -1])
def test_number_input(rpn, n):
    rpn.evaluate(str(n))
    assert rpn.stack == [n]


@pytest.mark.parametrize("op", ["**", "+-"])
def test_unknown_operator(capsys, rpn, op):
    rpn.stack = [1, 2]
    rpn.evaluate(op)  # FIXME how to test that this prints an error?
    out, err = capsys.readouterr()
    assert out.strip() == f"Invalid input: {op}"

def test_division_by_zero(capsys, rpn):
    rpn.stack = [1, 0]
    rpn.evaluate("/")  # FIXME how to test that this prints an error?
    out, err = capsys.readouterr()
    assert out.strip() == "Division by zero"

def test_not_enough_operands(capsys, rpn):
    rpn.stack = [1]
    rpn.evaluate("+")  # FIXME how to test that this prints an error?
    out, err = capsys.readouterr()
    assert out.strip() == "Not enough operands"

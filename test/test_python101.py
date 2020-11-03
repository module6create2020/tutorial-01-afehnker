import pytest
import ast
import inspect
from exercises.python101 import *


# No need to change these tests.
class TestExercise1_1_2_1:

    def test_foo(self):
        assert foo(), "Method foo() should return the value True"


class TestExercise1_1_3_1:

    @pytest.mark.parametrize("a,b,c", [(5, 8, 13), (5.5, 8.5, 14.), ("ab", "cd", "abcd")])
    def test_plus(self, a, b, c):
        result = concatenadd(a, b)
        if not result == c:
            pytest.fail("The method Concatenadd failed with arguments {} and {}. "
                        "Should have returned {}, but returned {}".format(a, b, c, result))


class TestExercise1_1_3_2:

    @pytest.mark.parametrize("frogs, clutch, color", [(1, -1, "blue"), (1, 0.5, "green"), (-3, -1.5, "white"),
                                                      (1, -0.5, "blue"), (-1, -0.5, "red"), (-1, -1.5, "black")])
    def test_cf_color(self, frogs, clutch, color):
        result = cf_color(frogs, clutch)
        if result != color:
            pytest.fail("The method cf_color failed, with {} and {} it "
                        "should have returned {}, but it returned {}.".format(frogs, clutch, color, result))


class TestExercise1_1_4_1:

    @pytest.mark.parametrize("x, y", [(5, 5), (7, 16), (19, 20)])
    def test_collatz(self, x, y):
        result = collatz(x)
        if result != y:
            pytest.fail("The method collatz failed, with {}, it should have returned {}, "
                        "but it returned {}.".format(x, y, result))


class TestExercise1_1_4_2:
    @pytest.mark.parametrize("x, y", [(5, 5), (7.5, 16), (-2, None), ("Ffdfd", None)])
    def test_typed_collatz(self, x, y):
        for x, y in [(5, 5), (7.5, 16), (-2, None), ("Ffdfd", None)]:
            result = collatz(x)
            if result != y:
                pytest.fail(
                    "The method collatz failed, with {}, it should have returned {}, but it returned {}.".format(x, y,
                                                                                                                 result))


class TestExercise1_1_5_1:

    def test_for_e(selfself):
        assert even_steven("This hovercraft is full of eels.") == "hshvrrf sfl fel.", "Not quite the right answer."

    def test_even_steven_for(self):
        if not (any(isinstance(node, ast.For) for node in ast.walk(ast.parse(inspect.getsource(even_steven))))):
            pytest.fail("The method even_steven() should contain a for loop!")


class TestExercise1_1_5_2:

    @pytest.mark.parametrize("x, y", [("Hello", "Heelloe"),
                                      (
                                      "This hovercraft is full of eels.", "Thies hoeveercraeft ies fuell oef eeeels.")])
    def test_extend_e(self, x, y):
        result = extend_e(x)
        if result != y:
            pytest.fail("The method 'extend_e' failed, with '{}', it should have returned "
                        "'{}', but it returned '{}'.".format(x, y, result))


class TestExercise1_1_5_3:
    @pytest.mark.parametrize("x, y", [("Yes, sure is", "No! Ooooh! Yeees, sueree ies"),
                                      ("What do you mean?", "None of your business. ")])
    def test_reply_argument(self, x, y):
        result = reply2argument(x)
        if result != y:
            pytest.fail(
                "The method 'reply2argument' failed, with '{}', it should have returned '{}', "
                "but it returned '{}'.".format(x, y, result))


if __name__ == "__main__":
    pytest

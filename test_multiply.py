#Test First TDD Cycle 1

# This was a failed test
# def test_multiply_1x1():
#     assert multiply(1, 1) == 1

from multiply import multiply
 # this test passed
def test_multiply_1x1():
    assert multiply(1, 1) == 1

#Test First TDD Cycle 2
def test_multiply_2x2():
    assert multiply(2, 2) == 4

#Test First TDD Cycle 3
def test_multiply_3x3():
    assert multiply(3, 3) == 9

#Fourth Test Cycle
def test_multiply_4x4():
    assert multiply(4, 4) == 16

#Fifth Test Cycle
def test_multiply_23x45():
    assert multiply(23, 45) == 1035
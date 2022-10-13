import pytest
from module.series import fibonacci
from module.series import lucas
from module.series import sum_series


# fibonacci
def test_zero_fibonacci():
    actual=fibonacci(0)
    expected=0
    assert actual==expected

def test_one_fibonacci():
    actual=fibonacci(1)
    expected=1
    assert actual==expected

def test_two_fibonacci():
    actual=fibonacci(2)
    expected=1
    assert actual==expected

def test_three_fibonacci():
    actual=fibonacci(3)
    expected=2
    assert actual==expected

def test_four_fibonacci():
    actual=fibonacci(4)
    expected=3
    assert actual==expected

def test_five_fibonacci():
    actual=fibonacci(5)
    expected=5
    assert actual==expected

def test_six_fibonacci():
    actual=fibonacci(6)
    expected=8
    assert actual==expected

def test_seven_fibonacci():
    actual=fibonacci(7)
    expected=13
    assert actual==expected

def test_zero_lucas():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_one_lucas():
    actual=lucas(1)
    expected=1
    assert actual==expected

def test_two_lucas():
    actual=lucas(2)
    expected=3
    assert actual==expected

def test_three_lucas():
    actual=lucas(3)
    expected=4
    assert actual==expected

def test_four_lucas():
    actual=lucas(4)
    expected=7
    assert actual==expected

def test_five_lucas():
    actual=lucas(5)
    expected=11
    assert actual==expected

def test_six_lucas():
    actual=lucas(6)
    expected=18
    assert actual==expected

def test_seven_lucas():
    actual=lucas(7)
    expected=29
    assert actual==expected
def test_four_lucas_sum_series():
    actual=sum_series(4,2,1)
    expected=7
    assert actual==expected

def test_five_fibonacci_sum_series():
    actual=sum_series(5,0,1)
    expected=5
    assert actual==expected

def test_five_lucas_sum_series():
    actual=sum_series(5,2,1)
    expected=11
    assert actual==expected

def test_six_fibonacci_sum_series():
    actual=sum_series(6,0,1)
    expected=8
    assert actual==expected

def test_six_lucas_sum_series():
    actual=sum_series(6,2,1)
    expected=18
    assert actual==expected

def test_seven_fibonacci_sum_series():
    actual=sum_series(7,0,1)
    expected=13
    assert actual==expected

def test_seven_lucas_sum_series():
    actual=sum_series(7,2,1)
    expected=29
    assert actual==expected    
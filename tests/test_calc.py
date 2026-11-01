from src.calc import average, median


def test_average():
    assert average([1, 2, 3]) == 2


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    # Bug 1: integer division turns 2.5 into 2.
    assert median([1, 2, 3, 4]) == 2.5


def test_median_keeps_input():
    # Bug 2: median() sorts the caller's list in place.
    data = [4, 1, 3, 2]
    median(data)
    assert data == [4, 1, 3, 2]

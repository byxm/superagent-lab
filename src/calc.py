"""Tiny module with two real bugs. The lab's job is to get the tests green."""


def average(values):
    """Return the arithmetic mean."""
    return sum(values) / len(values)


def median(values):
    """Return the middle value, or the mean of the two middle values."""
    values.sort()
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    return (values[n // 2 - 1] + values[n // 2]) // 2

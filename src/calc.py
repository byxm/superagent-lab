"""Tiny module with two real bugs. The lab's job is to get the tests green."""


def average(values):
    """Return the arithmetic mean."""
    return sum(values) / len(values)


def median(values):
    """Return the middle value, or the mean of the two middle values."""
    ordered = sorted(values)
    n = len(ordered)
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2

from argparse import ArgumentTypeError

import pytest

from app.aggregation import aggregate


def test_average_aggregate():
    rows = [[10], [20], [30]]
    columns = ["Score"]
    result = aggregate(rows, columns, "Score=avg")
    assert result[0] == "avg"
    assert abs(result[1] - 20.0) < 1e-6


def test_min_max_aggregate():
    rows = [[5], [15], [25]]
    columns = ["Value"]
    assert aggregate(rows, columns, "Value=min")[1] == 5
    assert aggregate(rows, columns, "Value=max")[1] == 25


def test_incorrect_format():
    rows = [[5],[10],[15]]
    columns = ["Value"]
    with pytest.raises(ArgumentTypeError):
        aggregate(rows, columns, "Value=sum")
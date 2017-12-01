import pytest

from advent.inverse_captcha import seq_sum, sum_half_seq

seq_sum_test_data = [
    (map(int, "1122"), 3),
    (map(int, "1111"), 4),
    (map(int, "1234"), 0),
    (map(int, "91212129"), 9),
]

sum_half_seq_test_data = [
    (map(int, "1212"), 6),
    (map(int, "1221"), 0),
    (map(int, "123425"), 4),
    (map(int, "123123"), 12),
    (map(int, "12131415"), 4),
]


@pytest.mark.parametrize("data,expected", seq_sum_test_data)
def test_seq_sum(data, expected):
    assert seq_sum(data) == expected


@pytest.mark.parametrize("data,expected", sum_half_seq_test_data)
def test_sum_half_seq(data, expected):
    assert sum_half_seq(data) == expected

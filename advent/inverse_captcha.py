#!/usr/bin/env python


def seq_sum(data):
    total = 0
    prev = None
    for d in data:
        if d == prev:
            total += d
        prev = d
    if len(data) > 1 and data[0] == data[-1]:
        total += data[0]
    return total


def sum_half_seq(data):
    total = 0
    length = len(data)
    step = length / 2
    for i, d in enumerate(data):
        if d == data[(i + step) % length]:
            total += d
    return total


def main():
    import fileinput
    data = map(int, next(fileinput.input()).strip())
    print seq_sum(data)
    print sum_half_seq(data)


if __name__ == "__main__":
    main()

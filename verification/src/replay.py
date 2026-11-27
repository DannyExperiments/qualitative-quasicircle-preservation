"""Exact finite replay of the affine example and a model plateau sequence."""
from fractions import Fraction as Q


def distance_squared(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def verify_example():
    z, a, b, w = (0, 0), (1, 0), (0, 1), (-1, -1)
    assert distance_squared(z, a) == distance_squared(z, b) == 1
    assert cross(z, a, b) == 1
    assert w[0] < 0 and b[0] == z[0] == 0 and a[0] > 0
    for stretch in range(1, 9):
        image = [(stretch * x, y) for x, y in (z, a, b, w)]
        z1, a1, b1, w1 = image
        assert distance_squared(z1, b1) == 1
        assert distance_squared(z1, a1) == stretch ** 2
        assert distance_squared(z1, w1) == stretch ** 2 + 1
    print("PASS: affine stretch 8 gives squared endpoint and arc witness distances 1, 64, 65")


def verify_plateaus():
    previous = None
    for index in range(1, 41):
        t = Q(1, 5 ** index)
        y = (-1) ** index * t / 4
        r = t / 120
        left, right = t - 8 * r, t + 8 * r
        assert 0 < left < t < right
        if previous is not None:
            old_t, old_y, old_left = previous
            assert t < old_t / 4
            assert old_left - right > Q(65, 100) * old_t
            assert abs(old_y - y) / (old_left - right) < Q(1, 2)
        previous = t, y, left
    print("PASS: 40 plateau disks obey the separation and interpolation slope estimates")


if __name__ == "__main__":
    verify_example()
    verify_plateaus()

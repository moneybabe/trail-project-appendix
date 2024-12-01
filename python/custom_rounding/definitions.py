import math

"""Rounding functions"""


def round_up(number):
    return math.nextafter(number, math.inf)


def round_down(number):
    return math.nextafter(number, -math.inf)


"""Auxiliary functions"""


def w(x):
    return (8 * x + 1) ** (1 / 2)


def upw(x):
    return round_up(w(x))


def downw(x):
    return round_down(w(x))


def s(x):
    return ((w(x) - 1) ** 2) / (4 * (w(x) + 7))


def ups(x):
    return round_up(((upw(x) - 1) ** 2) / (4 * (downw(x) + 7)))


def downs(x):
    return round_down(((downw(x) - 1) ** 2) / (4 * (upw(x) + 7)))


def s_inv(x):
    return 1 / s(1 / x)


def ups_inv(x):
    return round_up(1 / downs(1 / x))


def downs_inv(x):
    return round_down(1 / ups(1 / x))


"""Indexed auxiliary functions"""


def si(x, i=0):
    if i == 0:
        return x
    elif i > 0:
        inner = si(x, i - 1)
        return s(inner)
    else:
        inner = si(x, i + 1)
        return s_inv(inner)


def upsi(x, i=0):
    if i == 0:
        return round_up(x)
    elif i > 0:
        inner = upsi(x, i - 1)
        return ups(inner)
    else:
        inner = upsi(x, i + 1)
        return ups_inv(inner)


def downsi(x, i=0):
    if i == 0:
        return round_down(x)
    elif i > 0:
        inner = downsi(x, i - 1)
        return downs(inner)
    else:
        inner = downsi(x, i + 1)
        return downs_inv(inner)


def ci(x, i=0):
    inner = si(x, i)
    return ((w(inner) + 3) ** 2) / 16


def upci(x, i=0):
    inner = upsi(x, i)
    return round_up(((upw(inner) + 3) ** 2) / 16)


def downci(x, i=0):
    inner = downsi(x, i)
    return round_down(((downw(inner) + 3) ** 2) / 16)


def di(x, i=0):
    inner = si(x, i)
    return ((w(inner) + 3) ** 2) / (8 * (w(inner) + 1))


def updi(x, i=0):
    innerup = upsi(x, i)
    innerdown = downsi(x, i)
    return round_up(((upw(innerup) + 3) ** 2) / (8 * (downw(innerdown) + 1)))


def downdi(x, i=0):
    innerup = upsi(x, i)
    innerdown = downsi(x, i)
    return round_down(((downw(innerdown) + 3) ** 2) / (8 * (upw(innerup) + 1)))


"""Composite functions"""


def Pi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0:
        return 1
    else:
        return Pi(x, i - 1) + math.prod([ci(x, j) - 1 for j in range(0, i)])


def upPi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0:
        return 1
    else:
        return upPi(x, i - 1) + round_up(
            math.prod([upci(x, j) - 1 for j in range(0, i)])
        )


def downPi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0:
        return 1
    else:
        return downPi(x, i - 1) + round_down(
            math.prod([downci(x, j) - 1 for j in range(0, i)])
        )


def Si(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0:
        return 1
    else:
        return Si(x, i - 1) + math.prod([di(x, j) - 1 for j in range(0, i)])


def upSi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0:
        return 1
    else:
        return upSi(x, i - 1) + round_up(
            math.prod([updi(x, j) - 1 for j in range(0, i)])
        )


def downSi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0:
        return 1
    else:
        return downSi(x, i - 1) + round_down(
            math.prod([downdi(x, j) - 1 for j in range(0, i)])
        )


def Qi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0 or i == 1:
        return 0
    else:
        return Qi(x, i - 1) + math.prod([1 / (ci(x, -j) - 1) for j in range(1, i)])


def upQi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0 or i == 1:
        return 0
    else:
        return upQi(x, i - 1) + round_up(
            math.prod([1 / (downci(x, -j) - 1) for j in range(1, i)])
        )


def downQi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0 or i == 1:
        return 0
    else:
        return downQi(x, i - 1) + round_down(
            math.prod([1 / (upci(x, -j) - 1) for j in range(1, i)])
        )


def Ti(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0 or i == 1:
        return 0
    else:
        return Ti(x, i - 1) + math.prod([1 / (di(x, -j) - 1) for j in range(1, i)])


def upTi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0 or i == 1:
        return 0
    else:
        return upTi(x, i - 1) + round_up(
            math.prod([1 / (downdi(x, -j) - 1) for j in range(1, i)])
        )


def downTi(x, i=0):
    if i < 0:
        raise ValueError("i must be greater than or equal to 0")
    elif i == 0 or i == 1:
        return 0
    else:
        return downTi(x, i - 1) + round_down(
            math.prod([1 / (updi(x, -j) - 1) for j in range(1, i)])
        )


"""Mina margin map"""


def M(l, k, x):
    return (x * (Si(x, k) + Ti(x, l))) / (Pi(x, k) + Qi(x, l))


def calculate_bounds(a, b):
    upper = b * (Si(b, 4) + Ti(a, 5)) / (Pi(a, 4) + Qi(b, 5))
    lower = a * (Si(a, 4) + Ti(b, 5)) / (Pi(b, 4) + Qi(a, 5))
    return upper, lower


def calculate_rounded_bounds(a, b):
    upper = round_up(b * (upSi(b, 4) + upTi(a, 5)) / (downPi(a, 4) + downQi(b, 5)))
    lower = round_down(a * (downSi(a, 4) + downTi(b, 5)) / (upPi(b, 4) + upQi(a, 5)))
    return upper, lower

# -*-coding:utf-8-*-
def gcd(a, b):
    """
    求最大公约数。

    Args:
        a: 大于0并且是整数。
        b: 大于0并且是整数。

    Returns:
        返回结果。结果是最大公约数。

    Raises:
        IOError: 无错误。
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    求最小公倍数。

    Args:
        a: 大于0并且是整数。
        b: 大于0并且是整数。

    Returns:
        返回结果。结果是最小公倍数。

    Raises:
        IOError: 无错误。
    """
    return a * b // gcd(a, b)


def e_gcd(a, b):
    """
        扩展欧几里得定理。

        Args:
            a: 大于0并且是整数。
            b: 大于0并且是整数。

        Returns:
            返回结果。

        Raises:
            IOError: 无错误。
    """
    if b == 0:
        return 1, 0, a
    (x, y, r) = e_gcd(b, a % b)
    temp = x
    x = y
    y = temp - a // b * y
    return x, y, r


if __name__ == "__main__":
    print(lcm(56, 78))
    print(gcd(56, 78))
    print(e_gcd(5, 0))

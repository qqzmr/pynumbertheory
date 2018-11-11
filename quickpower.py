# -*-coding:utf-8-*-
def quick_power(a, b, c):
    """
    求快速幂。ret = a^b%c。

    Args:
        a: 底数。大于等于0并且是整数。
        b: 指数。大于等于0并且是整数。
        c: 模数。大于0并且是整数。

    Returns:
        返回结果。

    Raises:
        IOError: 无错误。
    """
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


if __name__ == "__main__":
    print(quick_power(44444444444, 1111111111111111111, 79))

# -*-coding:utf-8-*-
def quick_power(a, b, p):
    """
    求快速幂。ret = a^b%p。

    Args:
        a: 底数。大于等于0并且是整数。
        b: 指数。大于等于0并且是整数。
        p: 模数。大于0并且是整数。

    Returns:
        返回结果。

    Raises:
        IOError: 无错误。
    """
    a = a % p
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % p
        b >>= 1
        a = (a * a) % p
    return ans


if __name__ == "__main__":
    print(quick_power(44444444444, 1111111111111111111, 71))

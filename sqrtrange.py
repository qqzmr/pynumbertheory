# -*-coding:utf-8-*-
def get_sqrt_range(num):
    """
        求平方根范围。

        Args:
            num: 大于等于0并且是整数。

        Returns:
            返回元组，表示一个范围。平方根一定在这个范围之内。

        Raises:
            IOError: 无错误。
    """
    if num == 0:
        return 0, 0
    if num == 1:
        return 1, 1
    if num == 2 or num == 3:
        return 1, 2
    if num == 4:
        return 2, 2
    if num == 5 or num == 6 or num == 7 or num == 8:
        return 2, 3
    a = 1
    b = num - 1
    while 1:
        c = (a + b) // 2
        if c ** 2 > num:
            b = c
            if a ** 2 == num:
                return a, a
            if a + 1 == b:
                return a, b
        elif c ** 2 < num:
            a = c
            if b ** 2 == num:
                return b, b
            if a + 1 == b:
                return a, b
        else:
            return c, c


if __name__ == "__main__":
    print(get_sqrt_range(2**5000-1))

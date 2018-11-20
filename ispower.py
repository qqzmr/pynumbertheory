# -*-coding:utf-8-*-

import logrange


def _get_sqrt_range(num, b=0, index=2):
    """
        求num的index开方,index是指数，num是结果。求底数。

        Args:
            num: 大于等于0并且是整数。
            b: 大于等于0并且是整数。
            index: 大于等于0并且是整数。

        Returns:
            返回元组，表示一个开方范围。

        Raises:
            IOError: 无错误。
    """
    a = 1
    if b == 0:
        b = num - 1
    if num == 0:
        return 0, 0
    if num == 1:
        return 1, 1
    if num == 2 or num == 3:
        return 1, 2
    while 1:
        c = (a + b) // 2
        if c ** index > num:
            b = c
            if a ** index == num:
                return a, a
            if a + 1 == b:
                return a, b
        elif c ** index < num:
            a = c
            if b ** index == num:
                return b, b
            if a + 1 == b:
                return a, b
            if c == 1:
                return 1, 2
        else:
            return c, c


def is_power(num):
    """
        判断n是否是一个数的幂次方形式。

        Args:
            num: 大于等于0并且是整数。

        Returns:
            返回结果。true是幂数

        Raises:
            IOError: 无错误。
    """
    if num <= 3:
        return False
    else:
        bmax = logrange.get_log_range(num, 2)[1]
        bmin = 2
        b = bmin
        sqrt = 0
        temp = 0
        while b <= bmax:
            sqrt = _get_sqrt_range(num, temp, b)
            temp = sqrt[0]
            if sqrt[0] == sqrt[1]:
                return True
            if sqrt == (1, 2):
                return False
            b += 1
        return False


if __name__ == "__main__":
    print(is_power(2**10000+1))

# -*-coding:utf-8-*-


def get_log_range(num, basenum):
    """
        求对数范围。

        Args:
            num: 数，大于等于1并且是整数。
            basenum: 底数，大于等于2并且是整数。

        Returns:
            返回结果。对数范围。

        Raises:
            IOError: 无错误。
    """
    if num == 1:
        return 0, 0
    else:
        n = 0
        ism = 0
        while num >= basenum:
            if ism == 0 and num % basenum != 0:
                ism = 1
            n += 1
            num //= basenum
        return n, n + ism


if __name__ == "__main__":
    print(get_log_range(12319111111111111111, 4))

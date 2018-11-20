# -*-coding:utf-8-*-

import quickpower


def is_prime_trial_division(num):
    """
        判断是否是素数。试除法。

        Args:
            num: 大于等于2并且是整数。

        Returns:
            返回结果。true为素数；false是非素数。

        Raises:
            IOError: 无错误。
    """
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while num % i != 0:
        if i * i >= num:
            return True
        i = i + 2
    return False


def is_prime_fermat(num):
    """
        判断是否是素数。费尔马素性测试法（Fermat primality test） 可能会把合数误判为质数。

        Args:
            num: 大于等于2并且是整数。

        Returns:
            返回结果。true为素数；false是非素数。

        Raises:
            IOError: 无错误。
    """
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    if num % 2 == 0:
        return False
    if quickpower.quick_power(2, num - 1, num) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_prime_trial_division(12319))
    print(is_prime_fermat(2**256+1))

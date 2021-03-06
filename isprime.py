# -*-coding:utf-8-*-

import quickpower
import math
import time
from functools import wraps
#https://www.luogu.com.cn/problem/list?page=1 大量算法题

def timefn(fn):
    """计算性能的修饰器"""

    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1: .5f} s")
        return result

    return measure_time


@timefn
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


@timefn
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
    a = 2  # a是[2,num-1]之间的随机数
    if quickpower.quick_power(a, num - 1, num) == 1:
        return True
    else:
        return False


# 米勒-拉宾素性检验是一种概率算法，但是，Jim Sinclair发现了一组数：2, 325, 9375, 28178, 450775, 9780504, 1795265022。用它们做 [公式] ， [公式] 以内不会出错，我们使用这组数，就不用担心运气太差了。
@timefn
def is_prime_miller_rabin(num):
    """
        判断是否是素数。米勒拉宾素性检验是一种概率算法 可能会把合数误判为质数。

        Args:
            num: 大于等于2并且是整数。

        Returns:
            返回结果。true为素数；false是非素数。

        Raises:
            IOError: 无错误。
    """
    # num=(2^s)*t
    a = 2  # 2, 325, 9375, 28178, 450775, 9780504, 1795265022
    s = 0
    t = num - 1
    num_1 = t
    if not (num % 2):
        return False
    while not (t & 1):
        t >>= 1
        s += 1
    k = quickpower.quick_power(a, t, num)
    if k == 1:
        return True
    j = 0
    while j < s:
        if k == num_1:
            return True
        j += 1
        k = k * k % num
    return False


@timefn
def is_prime_comprehensive(num):
    """
        判断是否是素数。综合算法:试除法+米勒拉宾素性检验 可能会把合数误判为质数。

        Args:
            num: 大于等于2并且是整数。

        Returns:
            返回结果。true为素数；false是非素数。

        Raises:
            IOError: 无错误。
    """
    if num <= 1:
        return False
    if num & 1 == 0:
        return False

    # 100以内的质数表
    primeList = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # 质数表是否能整除
    for prime in primeList:
        if num == prime:
            return True
        if num % prime:
            if prime * prime >= num:
                return True
        else:
            return False

    # 米勒拉宾素性检验
    return is_prime_miller_rabin(num)


if __name__ == "__main__":
    # print(is_prime_trial_division(12319))
    # print(is_prime_trial_division(561))
    num = 1111111111111111111
    # num = 561 #合数
    # num = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    # num = 0xFFFFFFFFFFFF
    # FFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    num = 2 ** 10000 + 111
    print(is_prime_fermat(num))
    print(is_prime_miller_rabin(num))
    print("----------------------")
    print(is_prime_comprehensive(num))
# 如果n <2,047，则测试a = 2 就足够了；
# 如果n <1,373,653，则测试a = 2和3 就足够了；
# 如果n <9,080,191，则测试a = 31和73 就足够了；
# 如果n <25,326,001，则足以测试a = 2、3和5；
# 如果n <3,215,031,751，测试a = 2、3、5 和7 就足够了；
# 如果n <4,759,123,141，测试a = 2、7和61 就足够了；
# 如果n <3,474,749,660,383，测试a = 2、3、5、7、11 和13 就足够了；
# 如果n <341,550,071,728,321，则足以测试a = 2、3、5、7、11、13 和17。
# 如果n <3,825,123,056,546,413,051，则足以测试a = 2、3、5、7、11、13、17、19 和23

# https://blog.csdn.net/qq_42146775/article/details/102562329

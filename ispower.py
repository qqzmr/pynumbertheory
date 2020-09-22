# -*-coding:utf-8-*-
import logrange
import math
import time
from functools import wraps
def _get_sqrt_range(num, right, exp=2):
    """
        求num的exp开方,exp是指数，num是结果。求底数。
        Args:
            num: 大于等于0并且是整数。
            right: 大于等于0并且是整数。右边界。
            exp: 大于等于0并且是整数。
        Returns:
            返回元组，表示一个开方范围。
        Raises:
            IOError: 无错误。
    """
    left = 1
    if num == 0:
        return 0, 0
    if num == 1:
        return 1, 1
    if num == 2 or num == 3:
        return 1, 2
    while True:
        mid = (left + right) // 2
        if mid ** exp > num:
            right = mid
            if left ** exp == num:
                return left, left
            if left + 1 == right:
                return left, right
        elif mid ** exp < num:
            left = mid
            if right ** exp == num:
                return right, right
            if left + 1 == right:
                return left, right
            if mid == 1:
                return 1, 2
        else:
            return mid, mid

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
def is_power(num):
    return is_power2(num)
@timefn
def is_power1(num):
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
        log_range = logrange.get_log_range(num, 2)
        if log_range[0] == log_range[1]:
            return True
        expmax = log_range[0]
        expmin = 2
        exp = expmin
        sqrt = 0
        right = 2 ** (1 + log_range[0] // 2)
        while exp <= expmax:
            sqrt = _get_sqrt_range(num, right, exp)
            # right = sqrt[0]#缩小右边界范围
            if sqrt[0] == sqrt[1]:
                return True
            if sqrt == (1, 2):
                return False
            exp += 1
        return False

@timefn
def is_power2(num):
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
        log_range = logrange.get_log_range(num, 2)
        if log_range[0] == log_range[1]:
            return True
        expmax = log_range[0]
        expmin = 2
        exp = expmin
        sqrt = 0
        right = 2 ** (1 + log_range[0] // 2)
        while exp <= expmax:
            sqrt = _get_sqrt_range(num, right, exp)
            right = sqrt[0]  # 缩小右边界范围
            if sqrt[0] == sqrt[1]:
                return True
            if sqrt == (1, 2):
                return False
            exp += 1
        return False

@timefn
def is_power3(num):
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
        expmax=int(math.log(num,2))
        if num%4==0 and 2**expmax==num:
            return True
        expmin = 2
        exp=expmin
        while exp <= expmax:
            sqrt0=math.pow(num,1.0/2)
            sqrt=int(sqrt0)
            # print("底数a",sqrt)
            # print("指数exp", exp)
            # print(sqrt0)
            # print(sqrt**exp)
            # print("----")
            if sqrt == 1:
                return False
            if sqrt**exp==num:
                return True
            exp += 1
        return False

if __name__ == "__main__":
    num = 2 ** 100 + 1
    print(is_power(num))
    print(is_power2(num))
    print(is_power3(num))
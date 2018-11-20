# -*-coding:utf-8-*-

import quickpower


def is_have_sqrt_model(x, p):
    """
        是否有模平方根y*y=x mod p，已知x，p，判断是否存在y

        Args:
            x: 大于0并且小于p的整数。
            p: 质数。

        Returns:
            返回结果，true表示有模平方根；false表示没有模平方根。

        Raises:
            IOError: 无错误。
    """
    ret = quickpower.quick_power(x, (p-1)//2, p)
    if ret == 1:
        return True
    else:
        return False


def get_sqrt_model(x, p):
    """
        求模平方根y*y=x mod p，已知x，p求y

        Args:
            x: 大于0并且小于p的整数。
            p: 质数。

        Returns:
            返回结果y。

        Raises:
            IOError: 无错误。
    """
    if is_have_sqrt_model(x, p):
        t = 0
        # p-1=(2^t)*s //s是奇数
        s = p-1
        while s % 2 == 0:
            s = s // 2
            t = t + 1
        if t == 1:
            ret = quickpower.quick_power(x, (s+1)//2, p)
            return ret, p-ret
        elif t >= 2:
            x_ = quickpower.quick_power(x, p-2, p)
            n = 1
            while is_have_sqrt_model(n, p):
                n = n+1
            b = quickpower.quick_power(n, s, p)
            print(b)
            # t-1
            ret = quickpower.quick_power(x, (s+1)//2, p)
            t_ = 0
            while t-1 > 0:
                if quickpower.quick_power(x_*ret*ret, 2**(t-2), p):
                    pass
                else:
                    ret = ret*(b**(2**t_)) % p
                t = t - 1
                t_ = t_ + 1
            return ret, p-ret
        else:
            return -2, -2
    else:
        return -1, -1


if __name__ == "__main__":
    print(is_have_sqrt_model(200, 401))
    print(get_sqrt_model(200, 401))

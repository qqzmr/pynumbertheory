# -*-coding:utf-8-*-

import quickpower


def P_Q(P, Q, p):  # 计算P+Q P和Q不能相等
    k = (P[1] - Q[1]) * quickpower.quick_power(P[0] - Q[0], p - 2, p) % p  # P+Q 类似P点和Q和两个点的斜率
    ret0 = (k * k - P[0] - Q[0]) % p  # P+Q
    ret1 = (k * (P[0] - ret0) - P[1]) % p  # P+Q
    return ret0, ret1


def P_P(P, p):  # 计算2P
    k = ((3 * P[0] * P[0]) * quickpower.quick_power(2 * P[1], p - 2, p)) % p  # P+P 类似P点切线斜率
    ret0 = (k * k - 2 * P[0]) % p  # P+P
    ret1 = (k * (P[0] - ret0) - P[1]) % p  # P+P
    return ret0, ret1


if __name__ == "__main__":
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    P = (0xc6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5,
         0x1ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a)
    Q = (0xe493dbf1c10d80f3581e4904930b1404cc6c13900ee0758474fa94abe8c4cd13,
         0x51ed993ea0d455b75642e2098ea51448d967ae33bfbdfe40cfe97bdc47739922)
    ret = P_Q(P, Q, p)
    print("%x" % ret[0])
    print("%x" % ret[1])
    print("-" * 30)
    ret = P_P(P, p)
    print("%x" % ret[0])
    print("%x" % ret[1])

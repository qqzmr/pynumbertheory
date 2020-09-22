# -*-coding:utf-8-*-
import math
def quick_algorithm(a,b,c):  #y=a^b%c,a的b次幂余除c
    a = a % c
    ans = 1
    #这里我们不需要考虑b<0，因为分数没有取模运算
    while b != 0:  #费马小定理
        if b & 1:
            ans = (ans * a) % c
        b>>=1
        a = (a * a) % c
    return ans
def IsHaveMoSqrt(x,P):#是否有模平方根y*y=x mod p，已知x，p，判断是否存在y
    ret = quick_algorithm(x,(P-1)//2,P)
    if ret==1:
        return True
    else:
        return False
def GetMoSqrt(x,P):#求模平方根y*y=x mod p，已知x，p求y
    if(IsHaveMoSqrt(x,P)==1):
        t=0
        s=P-1#P-1=(2^t)*s //s是奇数
        while s%2==0:
            s=s//2
            t=t+1
        if(t==1):
            ret = quick_algorithm(x,(s+1)//2,P)
            return (ret,P-ret)
        elif (t>=2):
            x_=quick_algorithm(x,P-2,P)
            n=1
            while(IsHaveMoSqrt(n,P)==1):
                n=n+1
            b=quick_algorithm(n,s,P)
            print(b)
            ret = quick_algorithm(x,(s+1)//2,P)#t-1
            t_=0
            while(t-1>0):
                if(quick_algorithm(x_*ret*ret,2**(t-2),P)==1):
                    ret=ret
                else:
                    ret=ret*(b**(2**t_))%P
                t=t-1
                t_=t_+1
            return (ret,P-ret)
        else:
            return (-2,-2)
    else:
        return (-1,-1)
def Secp256k1GetYByX(x):#y^2=x^3+7 (mod p)根据x求y
     a=(x*x*x+7)%0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
     ret = GetMoSqrt(a,0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
     return ret
if __name__ == "__main__":
    ret = GetMoSqrt(200,401)
    print(ret)
    print("00000000000000000000000000000000000000000000000000")
    if True:
        x=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798#私钥为1,对应的公钥x
        ret = Secp256k1GetYByX(x)#secp256k1，根据x求y
        print("x=%x" % (x))
        print("y=%x" % (ret[0]))
        print("y=%x" % (ret[1]))
        print("")
        x=1#x最小值
        ret = Secp256k1GetYByX(x)#secp256k1，根据x求y
        print("x=%x" % (x))
        print("y=%x" % (ret[0]))
        print("y=%x" % (ret[1]))
        print("")
        x=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F-3#x最大值
        ret = Secp256k1GetYByX(x)#secp256k1，根据x求y
        print("x=%x" % (x))
        print("y=%x" % (ret[0]))
        print("y=%x" % (ret[1]))
        print("")
    input()
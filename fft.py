#def not copied from wikipedia
import math
import cmath

LICENSE_MESSAGE="""
    #############################################################
    #                                                           #
    #   This program is relased in the GNU GPL v3.0 license     #
    #   you can modify/use this program as you wish. Please     #
    #   link the original distribution of this software. If     #
    #   you plan to redistribute your modified/copied copy      #
    #   you need to relased the in GNU GPL v3.0 licence too     #
    #   according to the overmentioned licence.                 #
    #                                                           #
    #   "PROUDLY" MADE BY chkrr00k (i'm not THAT proud tbh)     #
    #                                                           #
    #############################################################
    #                                                           #
    #                                                           #
    #                            YEE                            #
    #                                                           #
    #                                                           #
    #############################################################
    """

def polar(r, t):
    return complex(r*math.cos(t), r*math.sin(t))
    
def log2(n):
    k = int(n)
    i = 0
    while k:
        k >>= 1
        i += 1
    return i-1

def check(n):
    return n > 0 and (n & (n - 1)) == 0

def reverse(m, n):
    j = 0
    p = 0
    for j in range(1, log2(m)+1):
        if int(n) & (1 << (log2(m) - j)):
            p |= 1 << (j - 1)
    return p

def sort(f1, n):
    return [f1[reverse(n, i)] for i in range(n)]

def transform(f, n):
    f = sort(f, n)
    w = [0]*(n//2)
    w[0] = 1
    w[1] = polar(1, -2*math.pi/n)

    for i in range(2, n//2):
        w[i] = w[1]**i
    nn = 1
    a = n//2
    for j in range(log2(n)):
        for i in range(n):
            if not (i & nn):
                t = f[i]
                T = w[(i*a)%(nn*a)]*f[i+nn]
                f[i] = t + T
                f[i+nn] = t - T
        nn *= 2
        a = a//2
    return f

def fft(f, d=1):
    if len(f) > 2 and check(len(f)):
        f = transform([float(e) for e in f], len(f))
        return [v*d for v in f]
    else:
        return [0]*len(f)

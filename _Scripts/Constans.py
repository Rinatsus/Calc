from numpy import *
import math


def get_int_or_float(num):
    if abs(int(num) - float(num)) == 0:
        return int(num)
    else:
        return float(num)


sin = math.sin
cos = math.cos
tan = math.tan
fac = math.factorial
pow = math.pow
abs = math.fabs

log = math.log10
ln = math.log

exp = math.exp
e = math.e
p = math.pi

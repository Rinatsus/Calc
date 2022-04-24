import math
import sympy as sym


def get_int_or_float(value):
    if sym.Mul(value):
        return value
    elif sym.Integer(value):
        return int(value)
    elif sym.Float(value):
        return float(value)


def get_points(nums, expr):
    arr = []
    x = sym.Symbol("x")
    for num in nums:
        temp = expr.subs(x, num)
        arr.append(temp)
    return arr


def get_point(num, expr):
    x = sym.Symbol("x")
    return expr.subs(x, num)


def get_formatted_expression(expr):
    new_expr = str(expr)
    if new_expr == '' or new_expr == '0':
        return sym.sympify(0)

    find = new_expr.rfind('=')
    if find != -1:
        left = new_expr[:find]
        rigth = new_expr[find + 1:]

        if (rigth == '0' or rigth == ''):
            new_expr = left
        else:
            new_expr = left + '-(' + rigth + ')'

    return sym.sympify(new_expr)


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

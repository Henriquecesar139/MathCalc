pi = float (3.141592653589793238462643383279502884197169399375)

def sum(values):
    try:
        result = 0
        for c in values:
            result = result + c
        return result
    except:
        return 'error'

def sub(values):
    try:
        result = values[0]
        values.pop(0)
        for c in values:
            result = result - c
        return result
    except:
        return 'error'

def mult(values):
    try:
        result = 1
        for c in values:
            result = result * c
        return result
    except:
        return 'error'

def div(values):
    try:
        result = values[0]
        values.pop(0)
        for c in values:
            result = result / c
        return result
    except:
        return 'error'

def sqrt(num, sqrt):
    try:
        return num ** (1 / sqrt)
    except:
        return 'error'

def expo(values):
    result = values[0]
    values.pop(0)
    for c in values:
        result = result ** c
    return result

def degree(num):
    try:
        return num * 180 / pi
    except:
        return 'error'

def radian(num):
    return num * pi / 180

def fah(num):
    return num * 9/5 + 32

def cel(num):
    return (num - 32) * 5/9

   
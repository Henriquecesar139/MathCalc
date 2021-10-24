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
    try:
        result = values[0]
        values.pop(0)
        for c in values:
            result = result ** c
        return result
    except:
        return 'error'

def degree(num):
    try:
        return num * 180 / pi
    except:
        return 'error'

def radian(num):
    try:
        return num * pi / 180
    except:
        return 'error'

def fah(num):
    try:
        return num * 9/5 + 32
    except:
        return 'error'

def cel(num):
    try:
        return (num - 32) * 5/9
    except:
        return 'error'
   
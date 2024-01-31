def decorator(origfunc):
    def wrapper(v0, v, t):
        a = origfunc(v0, v, t)
        S = (v0*t) + (a*(t*t) / 2)
        print(a, "- ускорение")
        print(S, "- расстояние")
    return wrapper


@decorator
def acceleration(v0, v, t):
    A = 0
    if (v0>v):
        A = (v0-v)/t
    elif (v0<v):
        A = (v-v0)/t
    return A

try:
    acceleration(0, 2, 2)
except ZeroDivisionError:
    print("t=0, деление на ноль запрещено. заверешение программы...")
except TypeError:
    print("данные не того типа.")






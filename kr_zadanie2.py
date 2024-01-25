def my_decorator(func):
    def wrapper(v0, v, t):


        uskr = func(v0, v, t)
        S = (v**2 - v0**2) / (2 * uskr)
        print(S)
    return wrapper

@my_decorator
def a(v0, v, t):
    return (v - v0) / t


try:
    V0 = int(input('vv V0'))
    V = int(input('vv V'))
    t = int(input('vv t'))
    a(V0,V,t)
except ZeroDivisionError:
    print("деление на ноль")
except TypeError:
    print("ты чё, тут только")



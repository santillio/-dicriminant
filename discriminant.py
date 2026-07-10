import math

def solve(a, b, c):
    eps = 1e-12
    a = float(a)
    b = float(b)
    c = float(c)

    if abs(a) < eps:
        # линейное или вырожденное уравнение
        if abs(b) < eps:
            if abs(c) < eps:
                return ("infinite",)
            return ()
        return (-c / b,)

    d = b * b - 4 * a * c
    if d < -eps:
        return ()
    if abs(d) <= eps:
        x = -b / (2 * a)
        return (x,)

    sqrt_d = math.sqrt(d)
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)
    return (x1, x2)


if __name__ == '__main__':
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    roots = solve(a, b, c)

    if roots == ():
        print("Корней нет")
    elif roots == ("infinite",):
        print("Бесконечно много решений")
    elif len(roots) == 1:
        print("Один корень: {:.6f}".format(roots[0]))
    else:
        print("Два корня: x1 = {:.6f}, x2 = {:.6f}".format(roots[0], roots[1]))


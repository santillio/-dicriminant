import math

def solve_vieta(a, b, c):
    """
    Решение квадратного уравнения с использованием теоремы Виета.
    По теореме Виета для уравнения ax² + bx + c = 0:
    - Сумма корней: x1 + x2 = -b/a
    - Произведение корней: x1 * x2 = c/a
    """
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

    # Вычисляем дискриминант
    d = b * b - 4 * a * c
    if d < -eps:
        return ()
    if abs(d) <= eps:
        x = -b / (2 * a)
        return (x,)

    # Находим оба корня
    sqrt_d = math.sqrt(d)
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)
    
    # Проверяем теорему Виета
    sum_roots = x1 + x2
    product_roots = x1 * x2
    
    expected_sum = -b / a
    expected_product = c / a
    
    # Сохраняем информацию о теореме Виета
    vieta_info = {
        'sum': sum_roots,
        'expected_sum': expected_sum,
        'product': product_roots,
        'expected_product': expected_product,
        'verified': (abs(sum_roots - expected_sum) < eps and 
                     abs(product_roots - expected_product) < eps)
    }
    
    return (x1, x2, vieta_info)


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
    
    print("\n=== Решение через дискриминант ===")
    roots = solve(a, b, c)

    if roots == ():
        print("Корней нет")
    elif roots == ("infinite",):
        print("Бесконечно много решений")
    elif len(roots) == 1:
        print("Один корень: {:.6f}".format(roots[0]))
    else:
        print("Два корня: x1 = {:.6f}, x2 = {:.6f}".format(roots[0], roots[1]))
    
    print("\n=== Решение по теореме Виета ===")
    result_vieta = solve_vieta(a, b, c)
    
    if result_vieta == ():
        print("Корней нет")
    elif result_vieta == ("infinite",):
        print("Бесконечно много решений")
    elif len(result_vieta) == 1:
        print("Один корень: {:.6f}".format(result_vieta[0]))
    else:
        x1, x2, vieta_info = result_vieta
        print("Два корня: x1 = {:.6f}, x2 = {:.6f}".format(x1, x2))
        print("\nПроверка теоремы Виета:")
        print("  Сумма корней: x1 + x2 = {:.6f}".format(vieta_info['sum']))
        print("  Ожидаемая сумма: -b/a = {:.6f}".format(vieta_info['expected_sum']))
        print("  Произведение корней: x1 * x2 = {:.6f}".format(vieta_info['product']))
        print("  Ожидаемое произведение: c/a = {:.6f}".format(vieta_info['expected_product']))
        if vieta_info['verified']:
            print("  ✓ Теорема Виета верна!")
        else:
            print("  ✗ Теорема Виета не верна (погрешность вычислений)")



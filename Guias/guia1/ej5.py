def potencia(a, b):
    if b == 0:
        return 1

    x = potencia(a, b // 2)

    if b % 2 == 0:
        return x * x
    else:
        return a * x * x
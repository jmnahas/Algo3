
def izquierdaDominante(x):
    n = len(x)
    if n == 2:
        if x[0] > x[1]:
            return print(True)
    if n > 2:
            izq=sum(x[:n//2])
            der=sum(x[n//2:])
            if izq > der:
                return izquierdaDominante(x[:n//2])
    return print(False)
izquierdaDominante([8, 9, 2, 3, 5, 6, 3, 2])
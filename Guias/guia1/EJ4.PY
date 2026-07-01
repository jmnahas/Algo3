def indiceEspejo(x,izq=0,der=None):
    if der is None:
        der = len(x) - 1
    if izq > der:
        return False

    mid = (izq + der) // 2

    if x[mid] == mid:
        return True
    elif x[mid] > mid:
        return indiceEspejo(x, izq, mid - 1)

    else:
        return indiceEspejo(x, mid + 1, der)

print(indiceEspejo([-5, -4, -3, -2, -1]))
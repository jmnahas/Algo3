def maxSubArray(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]

    medio = (inicio + fin) // 2

    izquierda = maxSubArray(arr, inicio, medio)
    derecha = maxSubArray(arr, medio + 1, fin)

    suma = 0
    mejor_izq = float("-inf")
    for i in range(medio, inicio - 1, -1):
        suma += arr[i]
        if suma > mejor_izq:
            mejor_izq = suma

    suma = 0
    mejor_der = float("-inf")
    for i in range(medio + 1, fin + 1):
        suma += arr[i]
        if suma > mejor_der:
            mejor_der = suma

    cruzado = mejor_izq + mejor_der

    return max(izquierda, derecha, cruzado)


arr = [3, -1, 4, 8, -2, 2, -7, 5]
print(maxSubArray(arr, 0, len(arr) - 1))
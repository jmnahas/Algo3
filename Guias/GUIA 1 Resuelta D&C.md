### **EJ1:**
#### 1.
El combine es linea 5 y toda la funcion merge
el divide la linea 5 
y el conquer es linea 6 y 7.

#### 2.
Se divide en 2 subprobelmas por eso hay 2 llamadas recursivas.

#### 3.
De la mitad del tamanio de arr

#### 4.
Tene costo n

####  5.
T(n)= 2T($n/2$)+f(n)

####  6.
T(n)=O(n log n)

### EJ2:

#### 1.
Combine no hay
divide es 5 y la comparacion
conquerr son 9 y 11

#### 2.
En 1 subproblema

#### 3.
la mitad del arr

#### 4.
ES de 0

#### 5.
T(n/2)+0

#### 6.
O(nlogn)

### EJ3:

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

### EJ4:

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

### Ej5:
def potencia(a, b):

    if b == 0:

        return 1

    x = potencia(a, b // 2)

    if b % 2 == 0:

        return x * x

    else:

        return a * x * x

### EJ6:

def MaximoMontana(x):

    if len(x)== 2:

        if x[0]>x[1]:

            return x[0]

        if x[1]>x[0]:

            return x[1]

    mid = len(x)//2

    if x[mid]>x[mid+1] and x[mid]<x[mid-1]:

        return MaximoMontana(x[:mid])

    if x[mid]>x[mid-1] and x[mid]<x[mid+1]:    

        return MaximoMontana(x[mid:])

    if x[mid]>x[mid-1] and x[mid]>x[mid+1]:

        return x[mid]

### EJ7:
1-
T(n)  
= T(n-2) + 5  
= T(n-4) + 5 + 5  
= T(n-6) + 5 + 5 + 5  
...

Entonces es O((n/2).5) Osea O(n)

2- T (n − 1) + n
Lo mismo que arriba nada mas que 
O(n.n) Osea O($n^2$)

3- No lo entendi

4- T (n − 1) + n^2
Caso similar al 2 termina dando O($n^3$)

5- 2T (n − 1)
Es algo similar al caso numero 1 por ejemplo, pero en este caso es 2.2.2.2.2.2.2 y asi.
Entonces la complejidad termina siendo O($2^n$)

6- T (n/2) + n
Este si es teorema maestro
a=1
b=2
f(n)= n

f(n) es mas grande que el resto de la funcion osea termina siendo O(n)

7-T (n/2) + √n
Igual que el 6
O($√n$)

8-Nuevamente mismo caso
O($n^2$)

9-Ahora es O($2^(n/4)$)

10- Aca es teo maestro pero no termina dominando f(n) sino lo otro y termina siendo n ^ log22 osea termina siendo O(n)

11-

12-
### EJ8:
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
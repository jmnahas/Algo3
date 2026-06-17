Esto se basa en dividir un problema en subproblemas del mismo tipo que el original, resolver los problemas mas pequenos y combinar las soluciones.
Las subpartes tienen que ser mas chicas, tienen que ser el mismo tipo de tarea, y dividir y combinar no pueden ser nulas, pero tampoco pueden ser muy costosas.
## Forma general de D&C
Se piensa en una formula, tipo F(X) donde X es el campo en donde voy a hacer el dividir(un array de numeros, una lista de alumnos, una lista de algo).Y que cuando se hace F(X) es la solucion al problema.

Si F(X) es lo suficientemente chico o simple se resuelve solo, sino se divide a X en $X_1,X_2,X_3,...X_K$.
Se hace el F($x_1$),F($x_2$),.....F($x_k$) cada uno de esos da un $Y_k$, se combinan los Y, y como resultado da una solucion de F(X).
### Cuanto tarda todo esto?
Se expresa en T($n$) y se consideran algunos factores: se divide en $a$ subproblemas de tamanio maximo n/c y que n/c > al primer elemento de n.
El costo de dividir y de unir los resultados. Y resolver los aT(n/c) subproblemas.
### Teorema Maestro
El Teorema maestro basicamente nos ahorra muchas cuentas de la complejidad y lo separa en algo muy simple.
Definimos T(n) como una funcion en partes, si n=1 Entonces T(1)=1 sino T(n)= aT(n/c) + f(n).
Siendo f(n) el costo de combinar y dividir resultados y a T(n/c) lo que vimos antes, c el tamanio de la subdivision de problemas y a la cantidad de subproblemas en los que se divide el problema. En un merge sort por ej, se generan 2 subproblemas cada vez que hago la funcion y cada uno se divide en 2 osea a es 2 y c es 2.
El teo maestro se divide en 3 casos.
f(n)=O($n^{log_ca-e}$) para e>0 entonces T(n)=O($n^{log_ca}$)
f(n)=O($n^{log_ca}$) entonces T(n)=O($n^{log_ca}\log\ n$ )
El tercero es medio al pedo.

### Un caso particular:Karatsuba
Lo que importa de todo esto es que termina diviendo en 3 subproblemas, todos de n/2 tamanio osea termina siendo O($n^{1,59}$)

### Programacion Dinamica, pa que?
Hay algo en el arbol de recusion que es la superoposicion de estados, se repiten los mismos estados de ir de las mismas o similares formas hacia la solucion final. Es por ello que se implementa una memoria la cual gracias a ella se ahorra complejidad y tiempo si por ejemplo tengo el factorial de 4! no voy a tener que calcular el 3! ni el 2! ni asi porque ya los calcule algun vez(o esa es la idea).
Hay 2 enfoques.
El top-down se implementa recursivamente pero se guardan los resultados de cada llamada en una memoria, si una llamada recursiva se repite se toma el resultado de esta estructura.
El bottom-up resuelve los subproblemas mas pequenios y guardamos todos los resultados para hacer los problemas mas grandes.

#### TOP DOWN
Una formula es esta:
![[Pasted image 20260605180632.png]]

Primero para hacer la funcion recursivo pensamos principalmente en los estados y en los casos base.
Luego nos fijamos si hay superposicion de problemas
![[Pasted image 20260605181506.png]]

Despues hay que pensar en la memoria la misma va a estar basdaa en la cantidad de estados y de parametros.

Por ultimo para definir la complejidad del algoritmo habria que hacer:
![[Pasted image 20260605182721.png]]
Otra forma de ver superposicion de problemas
![[Pasted image 20260605183003.png]]
Mas llamadas que estados, osea a la funcion f(n) se la llama mas veces que cantidad de estados posibles en cada llamada, entones hay llamados que repiten parametros.


#### BOTTOM-UP
Un ejemplo de como funciona Bottom-UP es en la sucession de fibonacci.
![[Pasted image 20260608113217.png]]

![[Pasted image 20260608113234.png]]
Osea,podemos ir calculando el paso siguiente atraves de los mas chicos, o no a traves pero teniendo como base los mas chicos.
En este caso y en otros lo que nos genera esto es un ahorro de memoria tambien, ya que ahora solamente necesito los dos casos anteriores para saber el n caso.










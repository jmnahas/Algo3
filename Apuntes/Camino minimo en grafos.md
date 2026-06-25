## Camino mínimo
Un camino minimo basicamente es si hay peso en las aristas del grafo, cual es el camino de A a B con la sumatoria menor posible
![[Pasted image 20260618150724.png]]

Hay 3 tipos de problemas de camino mínimo:
Único origen -> único origen
Único origen -> Multiples destinos
Multiples origenes -> multiples destinos

Hay 2 problemas a nivel de estructura/interpretacion:
Aristas con peso negativo:Algunos algoritmos no pueden tomar esto, ya que descomponen su funcionamiento.
Ciclos: Esto solo es un problema si se suma a lo anterior.

### Algoritmo de Dijkstra
Dijkstra es chad, agarra un vertice del cual se arranca y arranca a fijarse cuales son los vertice sque puede conectar que tiene mas cercanos con el menor peso posible, es parecido a Prim.
Dijkstra nos termina devolviendo:Un vector de predecesores(osea padres) y un vector de distancia minima de cada uno.
ej:
![[Pasted image 20260618152941.png]]
Este algoritmo no funciona con aristas de peso negativo ya que la misma podria presentarse despues de que se cerrase cual es el camino, y este no vuelve a probar eso.
Complejidad:O($n^2$) la trivial
Con un heap binario  O((m + n) log n)
Y usando heap de fibonacci  O(m + n log n)

### Algoritmo de Bellman-Ford
Este es mas raro, se va a ir fijando vertice por vertice las distnacias que puede lograr sumando una arista, y se va a fijando una por una hasta tener el menor camino verificando los vertices.
Este resuelve el tema de las aristas de peso negativo, no el de ciclos de peso negativo.

## Complejidades Caminos minimos uno a todos

Dijkstra (con cola de prioridad)|(O((V+E)\log V)
Dijkstra (sin heap)-(O($V^2$)
Bellman-Ford-(O($V * E$)


### Ejercicios
![[Pasted image 20260624121023.png]]
Este por ejemplo se puede resolver con bfs, ya que las calles no tienen un peso sino ir de una esquina a otro tiene.
Hacemos bfs desde todas las esquinas y nos vamos fijando cuales estan a mas de 5 de un nodo que tiene policias.
Eso es muy complejo, tambien podemos hacerlo solo desde las esquinas que tienen policias eso va a ser menos costosso. pero la mejor solucion es hacer un nodo fantasma al grafo y lo conectamos a todos los policias, ya desde ahi podemos ver cuales estan a 6 cuadras, y esas estan desprotegidas.

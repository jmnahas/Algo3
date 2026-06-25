## Flujovich
Las cosas de flujo lo que tienen es que cambaimos el modelado del grafo lo tenemos que epnsar de otra forma, ahora cada arista no siempre va a tener un peso siempre, las aristas van a tener capacidades para enviar y recibir flujo.
La idea de la resolucion de estos problemas es poder enviar la mayor cantidad de flujo de S a T, sabiendo que hay una capacidad maxima, no puedo enviar infinito siempre.
Nosotros para probar cosas tenemos los cortes que son basicamente una porcion del grafo pero sin los vertices siguientes, la capacidad de un corte es la sumatoria de las capacidad de las aristas salientes unicamente.
Entonces la idea de flujo es encontrar el valor de flujo maximo que es igual a la capacidad del corte minimo.


### El algoritmo de ford fulkerson
Este algo agarra la red residual(la red que dice basicamente cuanto tiene para entrar o salir flujo de cada vertice) y la va optimizando hasta el punto en donde no queden aristas entrantes en el nodo destino.
EJ:
![[Pasted image 20260625112645.png]]
![[Pasted image 20260625112705.png]]
![[Pasted image 20260625112723.png]]
LA complejidad es n U iteraciones donde U es la capacidad maxima del grafo.
Complejidad O($m.max(U)$)

### Algoritmo de Edmonds y Karp
Lo que hace este algoritmo es usar bfs para esas caminos de aumento, esto resuelve el problema en complejidad O($n.m^2$)

### Matching maximo en grafos bipartitos
Basicamente estos problemas son aquellos los cuales cada nodo solo puede tener una combinacion posible, entonces los imsmos terminan combinando y hacineod un grafo bipartito en donde se van perdiendo capacidades en el medio.

### Tips
![[Pasted image 20260625114323.png]]
![[Pasted image 20260625114349.png]]

Tenemos el mundo de las soluciones a nuestro problema abstracto y el mundo de resultados en nuestro modelo. Nos gustaria demostrar que la solucion optima a nuestro problema es equivalente a la solucion optima en nuestro modelo.
Una forma de mostrar eso es demostrar que los conjuntos de soluciones validas son iguales. Es decir, si A es el conjunto de soluciones validas al problema y B las soluciones validas en nuestro modelo, queremos ver que A = B, asi trivialmente el optimo va a ser igual en ambos lados.
En flujo suele ser comodo demostrar esto separando la ida y la vuelta.
Para mostrar que B ⊆ A, queremos, para cada cada solucion valida f al modelo, tener una soluci´on equivalente a nuestro problema. Por ejemplo, si lo que buscabamos era la mayor cantidad de caminos disjuntos en mapa, tenemosque mostrar que dado un flujo f en nuestro modelo hay un conjunto de |f |caminos disjuntos en nuestro problema.
Similarmente, para mostrar que A ⊆ B, tenemos que probar que para cadasolucion a nuestro problema podemos generar un flujo f de optimalidad equivalente.
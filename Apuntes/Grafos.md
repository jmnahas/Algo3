## Que son?
Los grafos modelan relaciones entre vertices, proporcionan una forma conveniente y flexible e representar problemas de la vida real como una red.Las redes pueden ser tangibles o intangibles.
Todo surge de los puentes de Konigsberg.El loco queria cruzar los 7 puentes que tenia 1 sola vez y llegar al punto de partida.No pudo

Teorema de los cuatro colores, este teorema plantea que todo mapa puede ser pintado en 4 colores, de modo tal que regiones limitrofes usen colores distintos.

#### Definiciones
Un grafo G(V,X) donde V es el conjunto de vertices y X el conjunto de aristas, cada arista tiene un incidencia como par ordenaddo, es decir culqueir elemento de X es (v,w) donde v y w son aristas.
La vecindad de un vertice N(v), es el conjunto de vertices adyacentes.
![[Pasted image 20260610190752.png]]

Mutigrafos es un grafo con mas de una arista a un mismo punto y pseudografo puede haber varias aristas y aparte puede haber loops de los vertices.

Grado:Es la cantidad de artistas incidentes a un vertice. $d_g(v1)$ es la cantidad de aristas incidentes a v.
El delta de G va a ser la arista con mayor grado y el omega de G la de menor.
![[Pasted image 20260610191102.png]]

En g2, el Delta es v1 y el omega v5,v6 o v7.
![[Pasted image 20260610192746.png]]

Grafo completo:Un Grafo es completo si todos sus vertices son adyacentes entre si.
Complemento:El complemento de un grafo es basicamente las aristas que no tiene el grafo.


#### Recorridos, caminos, circuitos y ciclos
Un recorrido es una secuencia lternada de vertices.

Un camino es un recorrido que no pasa dos veces por el mismo vertices
Una seccion es una subsecuencia de un camino.
Un circuito es un recorrido que arranca y termina en el mismo vertice
Un Ciclo o circuito simple es un circuito que tiene 3 o mas vertices que no pasa dos veces por el mismo vertice.
![[Pasted image 20260610193603.png]]

La longitud de un recorrido es la cantidad de aristas que tiene, entonces por ejemplo l(P1)=8.
La distancia entre dos vertices d(v,w) es la longitud del recorrido mas corto.
La distancia de (v,v)=0.
Un subgrafo es una porcion del grafo original.Si es inducido lo que sucede es que todas las aristas relacionadas a un vertice son eliminadas, si solamente elimina aristas es no inducido.

#### Grafo Conexo
Un grafo es conexo si existe camino entre todo par de vertices.
![[Pasted image 20260611104253.png]]

#### Grafo Bipartito
Un grafo es bipartito si existen dos subconjuntos de vetices tales que 
V1 U V2 = V, osea la union de estos dos conjuntos son todos los vertices del grafo
y V1 ^ V2= Vacio, osea la interseccion de estos dos es vacio.
Y encima, un grafo bipartito completo quiere decir que todo vertice de V1 es adyacente a V2.
![[Pasted image 20260611104619.png]]

#### Grafos Isomorfos
Dados dos Grafos, se dice que son isomorfos si existe una funcion a cual pueda llevar de un grafo al otro sin aniadir aristas o vertices.
Por ej:
![[Pasted image 20260611104928.png]]

Pero un ejemplo que no lo cumple:
![[Pasted image 20260611104952.png]]
![[Pasted image 20260611112034.png]]

Pero la vuelta de esto no vale, es decir si dos grafos cumplen todo esto no solamente por eso son isomorfos.

Un digrafo basicamente es un par de conjuntos donde las aritas tienen (u,w) donde w es la cabeza y u es la cola, w entonces es donde va dirigida la flecha y tiene grado de entrada +1 gracias a esto.
Despues esta el grado de salida, el cual es de donde salen las flechas.
![[Pasted image 20260611112238.png|195]]
Por ultimo existen lo mismo que en los grafos normales:Caminos(En donde solo paso por los que tienen grado de salida del vertice) y Circuitos (Arranco y termino en el mismo vertice)

Un grafo fuertemente Conexo es aquel que de todos sus componentes puedo llegar al resto.

## Representacion
Vamos a representar el grafo G como una **matriz de adyacencia** M de nxn
Si los vertices de la fila y la columna coinciden ponemos un 1.
Ej:
![[Pasted image 20260611114518.png]]

Despues siguen las complejidad de las cosas, por ejemplo con una matriz de adyacencia inicializar es  complejidad O($n^2$)
Para las aristas tenemos 3 procedimientos, ver si tiene arista, agregar una arista y eliminar una arista, para las 3 la complejidad es de O(1).
Por ultimo, para ver un vecindario es O(n).

Despues esta la **lista de adyacencia**
![[Pasted image 20260611114812.png]]
Esta tiene complejidad espacial menor.
Para inicializar tiene la misma complejidad O(n+m)
Para ver el vecindario es tan simple como traer la lista.
Para el tema de las aristas es un poco mas complicado:
![[Pasted image 20260611114956.png]]









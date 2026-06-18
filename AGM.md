### AGM clase teorica y practica
### Que es un agm?
Un arbol generador es un subgrafo de un G que es arbol.
Hay un teorema que dice 
![[Pasted image 20260618103818.png]]
Si las aristas del grafo tuvieran peso y se tiene que ver cual es el arbol generador mas chico, entonces ese sera su arbol generador minimo.

### Algoritmo de Prim
Este arranca con un vetice y va desde ese vertice haciendo todo el algormitmo yendo por la arista de menor peso, evaluando cual es la siguiente arista a agarrar que este conectando con un nodo no visto todavia.
El algoritmo de Prim es goloso.
Complejidad:O($n^2$) en la implementacion estandar
Usando heap es O((m+n)log n) o usando heap de FIbonacci O(m+ n log n)


### Algoritmo de Kruskal
Este no necesita un vertice, agarra la arista mas chica y empieza a elegir aristas del Grafo que conecten los vertices siendo siempre las mas chicas.
Complejidad:O(n . m)
Con Union and find es O(m log n + m log n)

### Camino MaxiMin
Un camino MaxiMin quiere decir la capacidad del Maximo de la menor arista(osea el camino que tiene la arista mas pequenia mas grande [Ej: entre el camino 7,6,6,8 y el 10,4,9,8 el MaxiMin es el primero ya que el 6 es mas grande que el 4])

### Camino MiniMax
Lo mismo pero al reves.
El ejemplo ahora podria ser 2,7 y 5,5 el camino minimax es el 5,5 ya que este aunque el peso del camino sea mayor la arista mas grande es menor a la mas grande del otro camino.

Entonces podemos decir que el camino MiniMax es: UN AGM

Algo que nos conviene hacer a veces es ocnstruir un grfo completo y despues correr prim o Kruskal, eso ayuda mucho un ejemplo es el ejercicio de las hormigas.
![[Pasted image 20260618112255.png]]
![[Pasted image 20260618112307.png]]
Aca puedo en ve de pensar cual es el meor lugar para poner un tubo, modelar como que todas las cuevas tienen tubo y de esa forma despues correr prim o kruskal y ver de que forma se podria conectar todas, lo que si hago un vertice fantasma que conecte con todos los tubos.



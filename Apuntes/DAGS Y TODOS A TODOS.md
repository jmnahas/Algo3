### Todos a todos
#### Floyd
Para los todos a todos tenemos algunas opciones, una de ellas es la de Floyd que basicamente agarra la matriz y se va fijando el camino minimo a medida que van pasando las iteraciones, osea hace muchas veces un a misma matriz y la va optimizando hasta el maximo. Usa programacion dinamica

#### Dantzig
Y despues tenemos Dantzig, usa la misma complejidad y va haciendo como un bottom-up de los pasos previos construye el siguiente, por eso es mas facil agregar vertices en este, y esa es una ventaja por sobre Floyd.

**Complejidad de ambos** : O($n^3$)
y de complejidad espacial ambos usan una matriz osea O($n^2$)

### Ejercicios Todos a Todos




### Dags
Un digrafo es un DAG si no tiene ciclos dirigidos
Como puedo saber si un grafo es Dag? DFS o BFS
Con el algoritmo de Kahn se puede usar el orden topologico y de esa forma se solucionan muchos problemas, o inviertiendo el post order de DFS.

Osea un gran tip para Dag es el hecho de pensar bien los grafos y la forma en la que no haya ciclos, si encuentro qeu el grafo que me dan no puede tener ciclos puede ser un DAG y por ende salir de alguna forma mas facil.
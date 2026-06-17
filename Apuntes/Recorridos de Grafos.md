### Recorridos
#### DFS
Dfs recorre en profundidad (Depth) osea primero va por todos los de la misma rama, y despues avanza de rama(si lo vemos como un arbol)
Complejidad: O(m+n)
#### BFS
Es lo mismo que Dfs pero en lo ancho, osea va por el mismo nivel primero despues se fija los vecinos de los vecinos.
Nos devuele un arbol v-geodesico, Devuelve todas as distancias de v a todos en el grafo.
Complejidad: O(m+n)

Si por ej: Quisieramos ver que un grafo es conexo, podemos hacer bfs o dfs y depsues fijarnos si todos los nodos fueron visitados.

Otro ej:Dar un algoritmo que dado un grafo devuelva la cantidad de componentes conexas que tiene.
Algo similar a lo anterior pero mas de una vez si en efecto tiene mas componentes conexas.

### Basicamente
Los ejercicios se suele hacer una lista de vertices visitados o por ejemplo cuantas veces se recorre el algoritmo para ver componentes conexas, se suele usar mas bfs porque da todas las distancias desde el vertice que se hace hacia todos en el grafo.
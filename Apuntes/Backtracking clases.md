
## Backtracking papa
La idea con backtracking basicamente es encontrar la mejor solucion de un conjunto de soluciones,existen soluciones parciales y soluciones factible(que son lo mismo pero que la parcial esta incompleta).
En un problema de optimizacion combinatoria hay muchas formas de un mismo conjunto por eso es combinatoria.
Los algoritmos de backtracking consisten en generar todas las soluciones factibles y quedarse con la mejor, suelen ser un generate and test(osea genero todo y voy probando)
El problema es que tiene complejidad exponencial.
Por ejemplo para el problema de la mochila, tengo que hacer muchos for hasta encontrar la solucion que tenga el mejor peso y beneficio posible.
Si yo solamente pusiese los ifs y la recursion asi nomas, seria un problema de **Fuerza Bruta**, pruebo todas las soluciones posibles y no me importa la complejidad, pero si por ejemplo agregase que no se puedan meter mas cosas cuando el peso de la mochila es excedido entonces ahi tenemos un backtracking.
Entonces el backtracking termina siendo recorrer las posibles configuraciones y descartar configuraciones parciales las cuales no puedan completarse a una solucion.
Por ejemplo en el problema de las damas, si no hiciese ninguna poda tendria en un $2^{64}$ combinaciones posibles(mucho), pero puedo ir haciendo podas, por ejemplo que dos damas no puedan estar en la misma casilla, ahi ya tengo (64 8) combinaciones.
Y si sabemos que no pueden estar en una misma columna tenemos $8^8$ combinaciones.
Por ultimo sabemos que cada fila solo puede tener una dama osea tenemos 8! combinaciones.
Esto termina acortando muchisimo las soluciones.


#### Arbol de recursion
Son los arboles con las soluciones parciales de las cosas, esta bueno porque sirve para visualizar las soluciones

![[Pasted image 20260602201357.png]]

#### Backtracking idea de ejercicios
Ahi me acorde, los ejercicios de backtracking son escribir la funcion con las podas y la recursion especificada. Pones los casos base y te divertis una banda.
![[Pasted image 20260602203919.png]]
EJ: 
Aca tengo que irme fijando que palabras son efectivamente palabras, entonces voy avanzando una palabra a la vez, si efectivamente se puede entonces voy a devolver true y va a ser cuando no queden mas palabras o la string sea nula. Sino va a seguir avanzando.
Sol:
![[Pasted image 20260602205616.png]]




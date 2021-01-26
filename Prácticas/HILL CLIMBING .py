#JUAN PABLO MARTINEZ ALVAREZ SISTEMAS EXPERTOS
#Problema del vendedor ambulante (TSP): RESOLVIENDOLO CON HC PARA BUSQUEDA
# dado un conjunto de ciudades y distancias entre cada par de ciudades,
#  el problema es encontrar la ruta más corta posible que visite cada ciudad exactamente una vez 
# y regrese al punto de partida. 
#IMPLEMENTADO CON ALGORITMO HC
"""
cada par de ciudades, el problema es encontrar la ruta más corta posible que visite cada ciudad exactamente una vez y regrese al punto de partida. 
Tenga en cuenta la diferencia entre el ciclo hamiltoniano y el TSP. El problema del ciclo hamiltoniano es averiguar si existe un recorrido que visite cada ciudad exactamente una vez. Aquí sabemos que existe el Hamiltonian Tour (porque el gráfico está completo) y, de hecho, existen muchos de estos tours, el problema es encontrar un ciclo hamiltoniano de peso mínimo. 
Por ejemplo, considere el gráfico que se muestra en la figura del lado derecho. Un recorrido de TSP en el gráfico es 1-2-4-3-1. El costo del tour es 10 + 25 + 30 + 15 que es 80.
El problema es un famoso problema NP-hard. No existe una solución conocida en tiempo polinómico para este problema.

"""

# Programa Python3 para implementar vendedor ambulante
# problema al utilizar un enfoque ingenuo. HC 
#LIBRERIAS IMPORTADAS
from sys import maxsize 
from itertools import permutations
V = 4
 
# implementación del problema del vendedor ambulante con HC
def travellingSalesmanProblem(graph, s): 
 
 # almacenar todos los vértices excepto el vértice de origen
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
   # almacenar el peso mínimo del ciclo Hamiltoniano
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
# almacenar el peso de la ruta actual (costo)
        current_pathweight = 0
 
# calcular el peso de la ruta actual
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
     # actualización mínima
        min_path = min(min_path, current_pathweight) 
         
    return min_path 
 
 
# Código del conductor
if __name__ == "__main__": 
 #VALOR DE LAS ARISTAS 
 #BUSCA LA RUTA MINIMA MAS CORTA

   
# representación matricial del gráfico
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]] 
    s = 0
#NODO A BUSCAR
    print(travellingSalesmanProblem(graph, s))

# COMO SALIDA DEBERIA DE DAR 8' YA QUE ES LA RUTA MINIMA CON EL CAMINO MAS CORTO 
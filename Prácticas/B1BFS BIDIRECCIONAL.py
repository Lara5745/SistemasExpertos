#JUAN PABLO MARTINEZ ALVAREZ SISTEMAS EXPERTOS
#La idea de la búsqueda bidireccional es ejecutar dos búsquedas simultáneas
#Mejor conocido como B1FS
"""
MEJOR CONOCIDO COMO B1FS
"""
#La búsqueda bidireccional se implementa teniendo una o dos búsquedas que comprueban antes de ser expandido si cada nodo está en la frontera del otro árbol de búsqueda

# Programa Python3 para BFS bidireccional
# Buscar para verificar la ruta entre dos vértices

# Definición de clase para nodo a
# ser agregado al gráfico
""" 
Suponga que queremos encontrar si existe un camino desde el vértice 0 al vértice 14.
 Aquí podemos ejecutar dos búsquedas, una desde el vértice 0 y otra desde el vértice 14. 
 Cuando tanto la búsqueda hacia adelante como hacia atrás se encuentran en el vértice 7, 
 sabemos que tenemos encontró una ruta del nodo 0 al 14 y la búsqueda se puede terminar ahora. 
 Podemos ver claramente que hemos evitado con éxito exploraciones innecesarias.
"""
class AdjacentNode:
	
	def __init__(self, vertex):
		
		self.vertex = vertex
		self.next = None

# Implementación de BidirectionalSearch
class BidirectionalSearch:
	
	def __init__(self, vertices):
	# Inicializar vértices y
	# gráfico con vértices
	
		self.vertices = vertices
		self.graph = [None] * self.vertices
		
		
	# Inicializando cola para reenvío
	# y búsqueda hacia atrás
		self.src_queue = list()
		self.dest_queue = list()
		
	
	# Inicializando fuente y
	# nodos de destino visitados como falso
		self.src_visited = [False] * self.vertices
		self.dest_visited = [False] * self.vertices
		
	# Inicializando origen y destino
	# nodos principales
		self.src_parent = [None] * self.vertices
		self.dest_parent = [None] * self.vertices
		
	# Función para agregar borde no dirigido
	def add_edge(self, src, dest):
		# Agregar bordes al gráfico

		# Agregar origen al destino
		node = AdjacentNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

	
	# Dado que el gráfico no está dirigido, sume
	# destino a origen
		node = AdjacentNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
		
	# Función para primera búsqueda de amplitud
	def bfs(self, direction = 'forward'):
		
		if direction == 'forward':
			
			# BFS in forward direction FUNCION PRINCIPAL 
			current = self.src_queue.pop(0)
			connected_node = self.graph[current]
			
			while connected_node:
				vertex = connected_node.vertex
				
				if not self.src_visited[vertex]:
					self.src_queue.append(vertex)
					self.src_visited[vertex] = True
					self.src_parent[vertex] = current
					
				connected_node = connected_node.next
		else:
			
			# BFS in backward direction
			current = self.dest_queue.pop(0)
			connected_node = self.graph[current]
			
			while connected_node:
				vertex = connected_node.vertex
				
				if not self.dest_visited[vertex]:
					self.dest_queue.append(vertex)
					self.dest_visited[vertex] = True
					self.dest_parent[vertex] = current
					
				connected_node = connected_node.next
				
	# Verifique el vértice que se cruza
	def is_intersecting(self):
		
	# Devuelve el nodo de intersección
	# si está presente else -1
		for i in range(self.vertices):
			if (self.src_visited[i] and
				self.dest_visited[i]):
				return i
				
		return -1

	# Imprime la ruta desde el origen al destino
	def print_path(self, intersecting_node, 
				src, dest):
						
	# Imprimir ruta final desde
	# origen a destino
		path = list()
		path.append(intersecting_node)
		i = intersecting_node
		
		while i != src:
			path.append(self.src_parent[i])
			i = self.src_parent[i]
			
		path = path[::-1]
		i = intersecting_node
		
		while i != dest:
			path.append(self.dest_parent[i])
			i = self.dest_parent[i]
			
		print("*****Path*****")
		path = list(map(str, path))
		
		print(' '.join(path))
	
	# Función para búsqueda bidireccional
	def bidirectional_search(self, src, dest):
		
	# Agregar fuente a la cola y marcar
	# visitado como Verdadero y agregue su
	# padre como -1	
		self.src_queue.append(src)
		self.src_visited[src] = True
		self.src_parent[src] = -1
	# Agregar destino a la cola y
	# marcar visitado como Verdadero y agregar
	# su padre como -1	
		self.dest_queue.append(dest)
		self.dest_visited[dest] = True
		self.dest_parent[dest] = -1

		while self.src_queue and self.dest_queue:
			
		# BFS en dirección de avance desde
		# Vértice de origen
			self.bfs(direction = 'forward')
			
		
		# BFS en sentido inverso
		# del vértice de destino
			self.bfs(direction = 'backward')
			
		# Verifique el vértice que se cruza
			intersecting_node = self.is_intersecting()
			
		# Si existe vértice que se cruza
		# luego la ruta desde la fuente hasta
		# destino existe
			if intersecting_node != -1:
				print(f"EXISTEN UN CAMINO ENTRE  {src} and {dest}")
				print(f"INTERSECCION EN  : {intersecting_node}")
				self.print_path(intersecting_node, 
								src, dest)
				exit(0)
		return -1

# Código del controlador
if __name__ == '__main__':
	
	# Número de vértices en el gráfico
	n = 15
	
	# Vértice de origen
	src = 0
	
	# Vértice de destino
	dest = 14
	
	# Crea un gráfico
	graph = BidirectionalSearch(n)
	graph.add_edge(0, 4)
	graph.add_edge(1, 4)
	graph.add_edge(2, 5)
	graph.add_edge(3, 5)
	graph.add_edge(4, 6)
	graph.add_edge(5, 6)
	graph.add_edge(6, 7)
	graph.add_edge(7, 8)
	graph.add_edge(8, 9)
	graph.add_edge(8, 10)
	graph.add_edge(9, 11)
	graph.add_edge(9, 12)
	graph.add_edge(10, 13)
	graph.add_edge(10, 14)
	
	out = graph.bidirectional_search(src, dest)
	
	if out == -1:
		print(f"NO EXISTE UN CAMINO ENTRE  {src} and {dest}")

"""
La búsqueda bidireccional reemplaza el gráfico de búsqueda único
 (que probablemente crezca exponencialmente) con dos subgráficos más pequeños, 
 uno que comienza desde el vértice inicial y otro que comienza desde el vértice del objetivo.
  La búsqueda termina cuando dos gráficos se cruzan.
"""
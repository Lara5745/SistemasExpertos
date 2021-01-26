class Arbol: 
    def __init__ (self, val, izq=None,der=None):
        self.valor = val
        self.izquierda = izq
        self.derecha = der

def buscar (valor,arbol):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if valor > arbol.valor:
        return buscar(valor,arbol.derecha)
    return buscar(valor,arbol.izquierda)

def enListar(arbol):
    if arbol == None:
        return []
    else:
        return enListar(arbol.izquierda)+[arbol.valor]+enListar(arbol.derecha)
    
def insertar(numero,arbol):
    if arbol == None:
        return Arbol(numero)
    if numero<arbol.valor:
        return Arbol(arbol.valor, insertar(numero,arbol.izquierda), arbol.derecha)
    else:
        return Arbol(arbol.valor, arbol.izquierda, insertar(numero,arbol.derecha))
    
def insertarLista(lista,arbol):
    if lista == []:
        return arbol
    else:
        return insertarLista(lista[1:],insertar(lista[0],arbol))
        
arbol1 = Arbol(12,Arbol(8,Arbol(4),Arbol(10,Arbol(9),Arbol(11))),
               Arbol(25,Arbol(8),Arbol(30,Arbol(28),Arbol(50))))

print(enListar(arbol1))
valor = int(input())
print(buscar(valor,arbol1))
#cprint(enListar(insertar(45,arbol1)))
#print(enListar(insertarLista([1,18,20],arbol1)))
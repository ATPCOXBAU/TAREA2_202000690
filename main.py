class Node:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None



class lcirculardoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero is None

    def unir(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def agregar(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Node(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Node(dato)
            self.ultimo.anterior = aux
        self.unir()

    def recorrer(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.dato)
            aux = aux.siguiente
        print(aux.dato)

    def buscar(self,dato):
        actual = self.primero
        while actual is not None:
            if actual.dato ==dato:
                print('Anterior: ', actual.anterior.dato, end=' ')
                print('Actual: ', actual.dato , end=' ')
                print('Siguiente: ', actual.siguiente.dato , end=' ')

                return True
            else:
                actual = actual.siguiente
                if actual == self.primero:
                    return False



if __name__ == '__main__':
    lista = lcirculardoble()
    lista.agregar(454)
    lista.agregar(88)
    lista.agregar(12)
    lista.agregar(47)
    lista.agregar(78)


    lista.recorrer()
    buscar = (int)(input('Seleccione numero: '))
    lista.buscar(buscar)




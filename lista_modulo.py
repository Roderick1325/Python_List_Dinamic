class Lista1():
    def __init__(self, dato, cadenas, lista):
        self.dato = dato
        self.cadenas = cadenas
        self.lista = []
    
    def agregar_lista(self):
        while int(self.dato) <= int(self.cadenas):
            if( self.dato <= self.cadenas):
                a = input("Ingresa una palabra: ")
                self.lista.append(a)
                self.dato += 1
    
    def imprimir(self):
        print("La lista tiene los siguientes datos: {}".format(self.lista))

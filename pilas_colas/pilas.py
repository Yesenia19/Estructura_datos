class Pila:
  print("Las pilas (stacks, en inglés) son TAD, esto es, Tipos Abstractos de Datos, que se estructuran en un formato de tipo lista a cuyos elementos se accede de una forma particular, tanto que tiene hasta su propio acrónimo en inglés: LIFO, de Last In, First Out, que podemos traducir como: Lo último en entrar (será) lo primero en salir")
  print("Ejemplo: ")
  def __init__(self):
    self.Top=None
    self.pila=[]

  def getTop(self): #obtenemos el ultimo elemento
    return self.Top

  def insertar(self, dato): #apilamos un dato a la pila
    self.Top=dato
    self.pila.append(dato)
    return self.Top
  
  def borrar(self): #desapilamos el ultimo elemento de la fila
    self.pila.pop()
    self.Top=self.pila[-1]
    return self.Top

  def __str__(self):
    return  str(self.pila)

  def __len__(self):
    return len(self.pila)

pila=Pila()
respuestas ="si"
while respuestas=="si":
    dato=int(input("Dato a ingresar: "))
    pila.insertar(dato)
    respuestas=input("Deseas agregar un elemento: ")

borrar=input("Deseas eliminar un elemento: ")
if borrar== "si":
  pila.borrar()


print("La pila final es:")
print(str(pila))
class Cola:
  print("Una cola es una variante de las pilas y, como ella, es también un TAD (recordemos, Tipos Abstractos de Datos). Representa una estructura de datos FIFO, del inglés, First In, First Out, donde el primer elemento en entrar (First in) es también el primer elemento en salir (First Out), al contrario de lo que sucede con las pilas (stacks) que, como acabamos de ver, representa una estructura de datos LIFO, donde el último elemento en entrar es también el primero en salir.")
  print("Ejemplo: ")
  def __init__(self):
    self.inicial=None
    self.final=None
    self.cola=[]

  def obtenerInicial(self): #obtenemos la primera pila ingresada
    return self.inicial
  
  def obtenerFinal(self):#obtenemos el valor final
    return self.final

  def insertar(self, dato): #insertamos un dato a la pila
    self.cola.append(dato)
    self.final=dato
    return self.final
  
  def borrar(self): #borramos la primera pila ingresada
    self.cola.pop(0)
    self.inicial=self.cola[0]
    return self.inicial

  def __str__(self):
    return str(self.cola)

  def __len__(self):
    return len(self.cola)

cola=Cola()
respuestas ="si"
while respuestas=="si":
    dato=int(input("Dato a ingresar: "))
    cola.insertar(dato)
    respuestas=input("Deseas agregar un elemento: ")

borrar=input("Deseas eliminar el primer elemento ingresado: ")
if borrar== "si":
  cola.borrar()

print("La cola final es:")
print(str(cola))
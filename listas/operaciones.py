def listaSimple():
  print("Este programa fue diseñado, ya que la maestra de Tecnologia, desea almacenar las participaciones de sus alumnos conforme partcipan  para posteriormente entregar un reporte")
  # Creamos la clase node
  class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

  # Creamos la clase linked_list
  class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("\n")

  s = linked_list() # Instancia de la clase
  ingresar="si"
  while ingresar == "si":
    dato=input("Valor a ingresar: ") 
    s.add_at_front(dato)
    ingresar=input("Desea agregar otro elemento: ")

  s.print_list() # Imprimimos la lista de nodos

def listaDoble():
  print("Este programa fue diseñado, ya que una pizzeria desea tener una lista en donde tenga los nombres de cada pizza, dependiendo su tamaño.")
    
  # Creamos la clase node
  class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
  class DoublyLinkedList():
    def __init__(self):
        self.start_node = None

    #Insertar elementos en una lista vacía
    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    #Insertar elementos al principio
    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    #Insertar elementos al final
    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    #Insertar artículo después de otro artículo
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    #Insertar artículo antes que otro artículo
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node
  
    #Recorrer una lista doblemente enlazada
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref
  
  new_linked_list = DoublyLinkedList()
  dato=int(input("Valor a ingresar: ")) 
  new_linked_list.insert_in_emptylist(dato)
  ingresar=input("Desea agregar otro elemento: ")
  while ingresar == "si":
    print("posiciones: \n 1)Insertar al inicio \n 2)Insertar al final \n 3)Insertar despues de otro elemento")
    opcion=int(input("Opcion a utilizar: "))
    if opcion == 1:
      dato=int(input("Valor a ingresar: ")) 
      new_linked_list.insert_at_start(dato)
    if opcion == 2:
      dato=int(input("Valor a ingresar: ")) 
      new_linked_list.insert_at_end(dato)
    if opcion == 3:
      print("Datos:")
      new_linked_list.traverse_list()
      dato=int(input("Valor a ingresar: "))
      elemento=int(input("Elemento de referencia: "))
      new_linked_list.insert_after_item(elemento,dato)
    if opcion > 3:
      print("Opcion invalida")
    ingresar=input("Desea agregar otro elemento: ")

  new_linked_list.traverse_list()

def listaCircular():
  print("Este programa fue diseñado, ya que se desea tener un control de como estaran sentados los asistentes en un debate, por lo que debemos tener una lista la cual no tenga un inicio o un final.")
  class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


  class CircularLinkedList:
    def __init__(self, head):
        self.head = head
        self.head.next = head

    #verifica si es el primer nodo de la lista
    def length(self):
        current = self.head.next
        count = 1
        if self.head is not None:
            while current != self.head:
                count += 1
                current = current.next
            return count
        else:
            return 0
    def search(self, position, prev=False):
        # Busca el elemento en la posición dada. Si position es negativo busca el último elemento
        # El argumento prev sirve para devolver en una lista tanto el nodo buscado como el anterior.
        if position == 0:
            if prev is False:
                return self.head
            else:
                return [self.search(-1), self.head]
        elif position < 0:
            current = self.head
            while current.next !=self.head:
                previous = current
                current = current.next
            return current if prev is False else [previous, current]
        else:
            k = 1
            current = self.head
            while k < position and current.next !=self.head:
                k += 1
                previous = current
                current = current.next
            return current if prev is False else [previous, current]

    #insertar elementos
    def insert(self, node, position):
        # Inserta el nodo después de la posición indicada. Si se indica una posición negativa, o mayor que
        # el tamaño de la lista, se inserta al final
        if position == 0:
            last_element = self.search(-1)
            last_element.next = node
            node.next = self.head
            self.head = node
        elif position < 0:
            last_element = self.search(-1)
            last_element.next = node
            node.next = self.head
        else:
            element = self.search(position)
            node.next = element.next
            element.next = node
    
  dato=input("Valor a ingresar: ")  
  c_list = CircularLinkedList(Node(dato))
  ingresar=input("Desea agregar otro elemento: ")
  while ingresar == "si":
    dato=input("Valor a ingresar: ") 
    posicion=int(input("Posicion a ingresar dato: "))
    c_list.insert(Node(dato), posicion)
    ingresar=input("Desea agregar otro elemento: ")

  print(c_list.head.data)
  current = c_list.head.next
  while current is not c_list.head:
    print(current.data)
    current = current.next



print("Opciones: \n 1)Programa 1 \n 2)Programa 2 \n 3)Programa 3")
resultado = int(input("Ingresa el numero de programa a utilizar: "))
if resultado==1:
  listaSimple()

if resultado==2:
  listaDoble()

if resultado==3:
  listaCircular()

if resultado > 3:
  print("La opcion es incorrecta")
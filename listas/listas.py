respuesta = 0
def listaSimple():
  print("Lista simple")
  print("Una lista enlazada simple es una estructura de datos en la que cada elemento apunta al siguiente. De este modo, teniendo la referencia del principio de la lista podemos acceder a todos los elementos de la misma.")
  print("Ejemplo:")

  # Creamos la clase node
  class node:
    def __init__(self, data = None, next = None):
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
    
    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("\n")


  s = linked_list() # Instancia de la clase
  s.add_at_front(5) # Agregamos un elemento al frente del nodo
  s.add_at_end(8) # Agregamos un elemento al final del nodo
  s.add_at_front(9) # Agregamos otro elemento al frente del nodo
  s.print_list() # Imprimimos la lista de nodos

def listaDoble():
  print("Lista doblemente enlazada")
  print("Una lista doblemente enlazada es una estructura de datos que consiste en un conjunto de nodos enlazados secuencialmente. Cada nodo contiene tres campos, dos para los llamados enlaces, que son referencias al nodo siguiente y al anterior en la secuencia de nodos, y otro más para el almacenamiento de la información (en este caso un entero). El enlace al nodo anterior del primer nodo y el enlace al nodo siguiente del último nodo, apuntan a un tipo de nodo que marca el final de la lista, normalmente un nodo centinela o puntero null, para facilitar el recorrido de la lista. Si existe un único nodo centinela, entonces la lista es circular a través del nodo centinela.")
  print("Ejemplo:")

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
  
    #eliminar elementos desde el principio
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;
  
    #Eliminar elementos del final
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
  
  new_linked_list = DoublyLinkedList()
  new_linked_list.insert_in_emptylist(50) #hacemos la funcion de Insertar
  new_linked_list.insert_at_end(49) #agregamos elementos al final
  new_linked_list.insert_at_start(5) #agregamos elementos al principio
  new_linked_list.insert_after_item(50, 65) #insertamos un elemento despues de otro
  new_linked_list.delete_at_start() #eliminamos un elemnto al principio
  new_linked_list.traverse_list()

def listaCircular():
  print("Lista circular")
  print("Consiste en una secuencia de nodos, en los que se guardan campos de datos arbitrarios y una o dos referencias, enlaces o punteros al nodo anterior o posterior. El principal beneficio de las listas enlazadas respecto a los vectores convencionales es que el orden de los elementos enlazados puede ser diferente al orden de almacenamiento en la memoria o el disco, permitiendo que el orden de recorrido de la lista sea diferente al de almacenamiento.")
  print("Ejemplo:")

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
    
    #eliminar elemntos
    def delete(self, position):
        # Para posiciones con valor negativo, borra el último nodo
        if position > 1:
            previous = self.search(position-1)
        elif position < 0:
            previous = self.search(-1, True)[0]
        else:
            previous = self.search(-1)
            self.head = previous.next.next
        previous.next = previous.next.next
    
  c_list = CircularLinkedList(Node(1))

  for i in range(2,15):
    c_list.insert(Node(i), i)
  c_list.delete(1)
  c_list.insert(Node(111), 0)
  c_list.delete(-1)
  c_list.insert(Node(999), -1)
  c_list.delete(3)

  print(c_list.head.data)
  current = c_list.head.next
  while current is not c_list.head:
    print(current.data)
    current = current.next

def fin():
  print("La opcion no es correcta")
  

print("Opciones: \n 1) Listas simples \n 2) Lista doblemente enlazada \n 3) Listas circulares")
respuesta = int(input("Ingresa el numero de lista a analizar: "))
if respuesta == 1:
  listaSimple()

if respuesta == 2:
  listaDoble()

if respuesta == 3:
  listaCircular()

if respuesta == 0:
  fin()
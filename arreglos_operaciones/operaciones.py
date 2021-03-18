import numpy as np #Importamos la libreria numpy 

arreglo1=[]  #Definimos un arreglo
arreglo2=[]
a_arreglo1=[]  #Definimos un arreglo para los nuevos valores del alineado
a_arreglo2=[]
f=0
c=0
opciones=7
def obtenerDatos():# Definimos un metodo para obtener los valores
  print("Arreglo 1")
  n_filas1 =int(input("Ingresa la cantidad de filas: ")) #pedimos la cantidad de filas del arreglo
  n_columnas1 =int(input("Ingresa la cantidad de columnas: ")) #pedimos la cantidad de columnas del arreglo

  for a in range(n_filas1):  # Definimos ciclos anidados
      arreglo1.append([])  #Asignamos una dimension en el vector
      for b in range(n_columnas1):    
        dato=input("Ingresa el dato del primer arreglo la posicion {},{}: ".format(a,b)) #Pedimos valores
        arreglo1[a].append(dato)  #Agregamos los datos al arreglo

  print("Arreglo 2")
  n_filas2 =int(input("Ingresa la cantidad de filas: ")) #pedimos la cantidad de filas del arreglo
  n_columnas2 =int(input("Ingresa la cantidad de columnas: ")) #pedimos la cantidad de columnas del arreglo

  for a in range(n_filas2):  # Definimos ciclos anidados
      arreglo2.append([])  #Asignamos una dimension en el vector
      for b in range(n_columnas2):    
        dato=input("Ingresa el dato del segundo arreglo en la posicion {},{}: ".format(a,b)) #Pedimos valores
        arreglo2[a].append(dato)  #Agregamos los datos al arreglo
  print("Arreglo 1")
  for elemento in (arreglo1): #mostramos el arreglo anterior
    print(elemento)
  print("Arreglo 2")
  for elemento in (arreglo2): #mostramos el arreglo anterior
    print(elemento)
  opciones=int(input("Numero de operacion que deseas utilizar: "))
  print("---------------------------------------------------------")  

def eliminarColumna(): #definimos la funcion para eliminiar una columna
  arreglo_utilizar=int(input("Numero de arreglo a utilizar para eliminar columna: "))
  if arreglo_utilizar == 1:
    eliminar=int(input("Columna a eliminar(0 es equivalente a la primer columna): "))  #Solicitamos la que desee eliminar
    matriz = np.delete(arreglo1, eliminar, axis = 1)  #La eliminamos 
    print("Actualizacion de matriz")
    print(matriz)

  if arreglo_utilizar == 2:
    eliminar=int(input("Columna a eliminar (0 es equivalente a la primer columna): "))  #Solicitamos la que desee eliminar
    matriz = np.delete(arreglo2, eliminar, axis = 1)  #La eliminamos 
    print("Actualizacion de matriz")
    print(matriz)
  opciones=int(input("Numero de operacion que deseas utilizar: "))
  print("---------------------------------------------------------")

def alinear():
  matriz1= np.array(arreglo1,int) 
  a_1=(matriz1.shape)
  matriz2= np.array(arreglo2,int) 
  a_2=(matriz2.shape)
  
  c_1=a_1[1]
  f_1=a_1[0]
  c_2=a_2[1]
  f_2=a_2[0]

  if (c_1 == c_2) and  (f_1 == f_2):
    c = 1
  

def suma_matriz():  
  if c == 1:
    #Las convertimos a tipo array
    matriz1= np.array(arreglo1,int) 
    matriz2= np.array(arreglo2,int)  
    print("La suma de matrices es: ")  
    suma=matriz1+matriz2 #Realizamos la operacion
    for element in suma:  #Mostramoslos resultados
      print(element)
  
  else:
    print("No se pueden sumar diferentes tamaños de matriz")
  opciones=int(input("Numero de operacion que deseas utilizar: "))
  print("---------------------------------------------------------")


def Multiplicacion_matrices():    #definimos multiplicar matrices
  if c == 1:
    #Las convertimos a tipo array
    matriz1= np.array(arreglo1,int) 
    matriz2= np.array(arreglo2,int)  
    print("La suma de matrices es: ")  
  #Realizamos la operacion
    multiplicacion=matriz1*matriz2
    for element in multiplicacion:
      print(element)
  
  else:
    print("No se pueden multiplicar diferentes tamaños de matriz")
  opciones=int(input("Numero de operacion que deseas utilizar: "))
  print("---------------------------------------------------------")

def matrizInvertida(): #Funcion para invertir
  opcion=int(input("Arreglo a invertir: "))
  matriz=0
  if opcion == 1:
    matriz= np.array(arreglo1,int)  #Convertimos a tipo array
    print("La matriz transpuesta es: ")  
    invertido=matriz.transpose()  #Aplicamos la funcion transpose
    for element in invertido: #Mostramos el resultado
      print(element)
  if opcion == 2:
    matriz= np.array(arreglo2,int)  #Convertimos a tipo array
    print("La matriz transpuesta es: ")  
    invertido=matriz.transpose()  #Aplicamos la funcion transpose
    for element in invertido: #Mostramos el resultado
      print(element)
  opciones=int(input("Numero de operacion que deseas utilizar: "))
  print("---------------------------------------------------------")

def diagonal():  
  opcion=int(input("Arreglo a utilizar: "))
  if opcion == 1:
    #Las convertimos a tipo array
    diagonal = np.diag(arreglo1)
    print(diagonal)
  if opcion == 2:
    #Las convertimos a tipo array
    diagonal = np.diag(arreglo2)
    print(diagonal)
  opciones=int(input("Numero de operacion que deseas utilizar: "))
  print("---------------------------------------------------------")

def fin():
  print("Gracias por tu tiempo")

obtenerDatos()
print("1 = Multiplicacion de matrices")
print("2 = Eliminar columna")
print("3 = Suma de matrices")
print("4 = Matriz invertida")
print("5 = Diagonal de una matriz")
opciones=int(input("Numero de operacion que deseas utilizar: "))
if opciones==1:
  Multiplicacion_matrices()
if opciones==2:
  eliminarColumna()
if opciones==3:
  suma_matriz()
if opciones == 4:
  matrizInvertida()
if opciones == 5:
  diagonal()
if opciones == 6:
  fin()
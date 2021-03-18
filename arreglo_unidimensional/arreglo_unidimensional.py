class Arreglos: # definimos una clase
  arreglo_1=[]
  arreglo_2=[]

  def __init__ (self): # definimos nuestro constructor
    pass
  
  def ingresarDatos (self):# definimos nuestro el metodo para ingresar los datos del arreglo
    arreglo_tamaño= int(input("Ingrese la cantidad de datos a ingresar: ")) #definimos la cantidad de datos a ingresar
    negativos=0  #declaramos variable para numeros negativos
    positivos=0  #declaramos variable para numeros positivos
    posicion_correcta=[] #declaramos un arreglo para las posiciones en el arreglo 1
    posicion_inversa=[] #declaramos un arreglo para las posiciones en el arreglo 2

    for i in range(arreglo_tamaño): #mediante un ciclo pedimos nuestros datos
      valor = int(input("Dato {} a ingresar: ".format(i+1)))
      if valor < 0: #definimos si es negativo
        negativos+=1 
      
      elif valor > 0: #definimos si es positivo
        positivos+=1

      elif valor ==0 : #definimos en que posicion esta si es 0
        posicion_correcta.append(i)


      self.arreglo_1.append(valor)

    tamaño=len(self.arreglo_1)
    
    while(tamaño>0): #leemos los datos del array
      tamaño-=1
      self.arreglo_2.append(self.arreglo_1[tamaño]) #los agregamos al segundo arreglo de forma inversa
      if (self.arreglo_1[tamaño]) == 0: #definimos si el valor es 0
        posicion_inversa.append((arreglo_tamaño-1)-(tamaño)) #definimos en que posicion esta si es 0 

    """imprimimos valores obtenidos""" 
    print("Los valores obtenidos en el primer arreglo son: {}".format(self.arreglo_1))
    print("Los valores obtenidos en el segundo arreglo son: {}".format(self.arreglo_2))
    print("Se encontraron {} numeros negativos".format(negativos))
    print("Se encontraron {} numeros positivos".format(positivos))
    print("El numero 0 se encontro en el arreglo 1 en la posicion {}".format(posicion_correcta))
    print("El numero 0 se encontro en el arreglo 2 en la posicion {}".format(posicion_inversa))


""" llamamos a nuestra funcion """
objeto=Arreglos()
objeto.ingresarDatos()
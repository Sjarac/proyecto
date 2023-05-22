#lista = [15, "nombre", 3.1415, True]
#print(lista)
#print(lista[0])

numeros = [10,50,100,255,500]

#Append = Agrega valores a la ultima posicion de la lista
numeros.append(1000)
print (f"{numeros}\n")

#Extends = Agrega un arreglo al final de la lista
extra = [75,350,999]
numeros.extend(extra)
print (f"{numeros}\n")

#Insert = Agrega valores en posiciones especificas
numeros.insert(6,5000)
print (f"{numeros}\n")

#Remove = Elimina el valor elegido de la lista
numeros.remove(50)
print (f"{numeros}\n")

#Pop = Elimina el ultimo registro
#Pop(i) = Elimina la posicion del valor
numeros.pop()
print (numeros)
numeros.pop(3)
print (f"{numeros}\n")

#Reverse = Invierte el orden de la lista
numeros.reverse()
print (f"{numeros}\n")

#Sort = Ordena los valores de menor a mayor
#Sort(Reverse=True) = Ordena los valores de mayor a menor
numeros.sort()
print (numeros)
numeros.sort(reverse=True)
print (f"{numeros}\n")
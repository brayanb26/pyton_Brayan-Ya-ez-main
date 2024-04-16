#eliiminar numeros duplicados de una lista 

lista = [2,4,4,6,2,5]         #creo una lista con numeros repetidos 
lista2 = []                          # copio los primeros elementos de la lista 1 en la lista 2
for i in range (len(lista)+1):       #creo un ciclo for con la funcion "len" que sirve para determinar el tamaño de una lista 
    if i in lista:
        lista2.append(i)

lista2.sort                           #agregamos la funcion sort a lista2 para ordenar la lista de forma ascendente

print(lista2)                        #imprimimos la lista 2 cpoon elementos repetidos ya eliminados


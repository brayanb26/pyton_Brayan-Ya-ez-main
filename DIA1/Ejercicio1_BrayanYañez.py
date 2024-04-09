#--------------------------------
#---- DIA 1 CHEAT SHEET PYTHON ------
#--------------------------------

#Imprimir hola mundo
print("Hola mundoooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#TRANAJO PEDIDO 

#Ingresa por teclado la infomarcion

print ("")
print ("ingresa tu nombre")
nombre = input ()
print ("bienvenido", nombre, ".gracias por usar el programa",sep="")


#Conversion de tipos de variable

numeroentero= 10
numeroflotante= float (numeroentero)
print (numeroflotante)

#Bucles For y While

#---bucle for 

nombre = ("brayan, daniel, dana")
for nombre in nombre
print (nombre)

#---bucle while 

suma = 0 
i = 1
while i <= 10:
    i+=1
    print (suma)


#Funciones (4 Tipos)

#funcion sin parametros o retornos de valores 

def dihola ():
   print ("hola")

dihola () #llama la funcion, "hola" se muestra en la consola

#funcion con parametro 

def holaconnombre(nombre):
    print ("hola"+nombre+"!")

holaconnombre ("brayan") #llama la funcion, "hola brayan" se muestra en la consola 

#funcion con multiples parametros con sentocia de retorno

def multiplica(val1, val2)
    return val1*val2
multiplica(3, 5) #muestra 15 en la consola 







#Desarrollado por Brayan Yañez c.c 1093925543
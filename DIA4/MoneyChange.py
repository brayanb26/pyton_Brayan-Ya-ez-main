print("algoritmo utilizado por cajeros en el mundo") #nombre del algoritmo que vamos a utiliozar

def valor_de_monedas(monto):               #definimos la funcion y los valores que le vamos a dar 
    nominaciones = [10, 5, 1]              #valores de las monedas en denomonaciones de 10,5,1
    monedas = 0

    for i in range(len(nominaciones)):
        nominacion = nominaciones[i]            #nominaciones 

        monedas += int(monto / nominacion)        #operacion
        monto = int(monto % nominacion) 
    return monedas                           #añadimos la funcion return para que realize la operacion 
monto = input("ingrese el monto a cambiar en monedas:")

nominaciones= [10, 5, 1]
pesos= int(monto.split(".")[0])
denominaciones_monedas= pesos
for i in range(len(nominaciones)):
    moneditas=denominaciones_monedas//nominaciones[i]
    if moneditas>0 : 
        print(moneditas, "monedas de ", pesos )

  


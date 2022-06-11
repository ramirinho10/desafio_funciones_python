def productoria(lista):
    resultado = 1
    for i in lista:
        resultado = resultado * i
    return resultado

def factorial(num):
    resultado = 1
    for i in range(num):
        resultado = resultado * (i+1)
    return resultado

#Me falta como realizarla // no se me ocurrio 
#Una función que permita controlar los cálculos. Esta función se debe invocar de la siguiente manera
#calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

def calcular(*calc):
    pass
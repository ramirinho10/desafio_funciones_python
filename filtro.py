import sys

umbral = float(sys.argv[1])

precios = {'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral, mayor = True):
    if mayor:
        filtro = []
        for k,v in diccionario.items():
            if v > umbral:
                filtro.append(k)
        print(f"Los productos mayores al umbral son: {', '.join(filtro)}")

        """
        filtro = [k for k,v in diccionario.items() if v > umbral]
        """
    else:
        filtro = []
        for k,v in diccionario.items():
            if v < umbral:
                filtro.append(k)
        print(f"Los productos menores al umbral son: {', '.join(filtro)}")

        """
        filtro = [k for k,v in diccionario.items() if v < umbral]
        """



if len(sys.argv) == 2:
    filtrar(precios, umbral)
else:
    if sys.argv[2] == "mayor":
        filtrar(precios, umbral, True)
    elif sys.argv[2] == "menor":
        filtrar(precios, umbral, False)
    else:
        print(f"Opcion no valida")



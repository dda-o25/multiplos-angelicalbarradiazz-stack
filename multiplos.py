"""
Inserta el encabezado aquí y escribe tu código abajo

    Determina si uno de los dos números enteros es múltiplo del otro.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        str: Mensaje indicando si a es múltiplo de b, b es múltiplo de a,
             o si ninguno lo es.
"""









# Entradas
#entrada = input()
try:
    numero1=int(input("Escribe el primer número y que sea entero por favor "))
    numero2=int(input("Escribe el segundo número y que sea entero también por favor "))

    # Declaraciones
    numerouno= str(numero1)
    numerodos=str(numero2)

    mensajesiesmultiplo1= (("El número ") + (numerouno)+(" es múltiplo del ")  + (numerodos))
    mensajesiesmultiplo2= (("El número ")  + (numerodos)+(" es múltiplo del ")  + (numerouno))
    mensajesiningunoesmultiplo= ("Ninguno de los números es múltiplo del otro")





    # Proceso

    #if not isinstance(numerouno, int) or not isinstance(numerodos, int):
    #  salida=("Hazme caso y pon un entero porfa")
    
    if numero2==0 or numero1==0:
        salida= "Ninguno de los números es múltiplo del otro"
    
    elif (numero1/numero2 == numero1//numero2):

        salida= mensajesiesmultiplo1

    elif (numero2/numero1== numero2//numero1):
        salida= mensajesiesmultiplo2
      
    else:
        salida= "Ninguno de los números es múltiplo del otro"


    # Salidas
    print(salida)

except ValueError:
    salida = "Ninguno de los números es múltiplo del otro"



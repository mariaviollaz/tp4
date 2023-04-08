#Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro

"""def print_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("Los números primos entre 1 y", n, "son:", primes)
n=int(input("ingrese un numero"))
print_primes(n)"""

#Escriba una función que le pida al usuario ingresar condimentos para un sándwich,
#hasta que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un
#mensaje avisando que ya se agregó el condimento al sándwich.
"""def armar_sandwich():
    condimentos = []
    condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
    
    while condimento.lower() != "salir":
        condimentos.append(condimento)
        print("Se ha agregado {} al sándwich.".format(condimento))
        condimento = input("Ingrese otro condimento para el sándwich (o 'salir' para terminar): ")
    
    print("El sándwich está listo, contiene los siguientes condimentos: {}".format(condimentos))
armar_sandwich()"""

#Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave

"""def hacer_remera(tamaño, mensaje):
    print("La remera es de tamaño", tamaño, "y tiene impreso el mensaje:", mensaje)

# Llamada a la función usando argumentos por posición
hacer_remera("M", "¡Soy una remera!")

# Llamada a la función usando argumentos por clave
hacer_remera(mensaje="¡Soy otra remera!", tamaño="L")"""

#Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes.

"""def hacer_remera(mensaje="Me gusta Python", tamaño="L"):

    print("La remera es de tamaño", tamaño, "y tiene impreso el mensaje:", mensaje)

# Llamada a la función con los valores por defecto
hacer_remera()

# Llamada a la función con valores diferentes
hacer_remera("¡Hola mundo!", "M")"""

#Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)

"""def fibonacci(n):
    primero=0
    segundo=1
    lista=[primero, segundo]
    for numero in range(n):
        tersero=primero+segundo
        lista.append(tersero)
        primero=segundo
        segundo=tersero
        numero=+1
        print(numero)
        print(lista)

n=int(input("ingresa un numero"))
fibonacci(n)"""

# Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
#la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
#el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
#calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc

def calculadora(primernumero,segundonumero,tercernumero):
    if tercernumero ==1:
      multipicacion=int(primernumero)*int(segundonumero)
      print(multipicacion)
    elif tercernumero==2:
     divicion=int(primernumero)/int(segundonumero)
     print(divicion)
    elif tercernumero==3:
     suma=int(primernumero)+int(segundonumero)
     print(suma)
    elif tercernumero==4:
      resta=int(primernumero)-int(segundonumero)
      print(resta)

primernumero=input("ingresar numero")
segundonumero=input("ingresar numero")
tersernumero=int(input("ingresa 1 pra *,2 para/, 3 para +, 4 para -"))
calculadora(primernumero,segundonumero,tersernumero)
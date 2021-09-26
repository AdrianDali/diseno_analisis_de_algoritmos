numeros = [1,2,3]

def unaFuncionCualquiera( lista ):
    conteo = 0 #O(1)
    suma = 0 #O(1)
    for num in lista:
        suma += num # O(n)
    print(f"La sumatoria de los numeros en la lista es={ suma } ") 
    # O(1)

    for numero1 in lista:
        for numero2 in lista:
            print(numero1 , numero2 ) #O(n^2)
            conteo += 1  #O(n^2)
    return conteo
#O( 3 + n +  2n^2)
#O( n + n^2)
#O(n^2)

conteo = unaFuncionCualquiera(numeros)

print( "Final:" , conteo)

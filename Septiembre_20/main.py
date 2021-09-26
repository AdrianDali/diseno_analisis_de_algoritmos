numeros = [1,2,3,4,5,6,7,8,9]

def unaFuncionCualquiera( lista ):
    conteo = 0 # O(1)
    for numero1 in lista:
        for numero2 in lista:
            print(numero1 , numero2 ) #O(n^2)
            conteo += 1  #O(n^2)
    return conteo
    # O(1 + 2n^2)

conteo = unaFuncionCualquiera(numeros)

print( "Final:" , conteo)
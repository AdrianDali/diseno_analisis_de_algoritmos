numeros = [1,2,3]
numeros2 = [4,5,6]

def unaFuncionCualquiera( lista,lista2 ):
    conteo = 0 #O(1)
    
    for numero1 in lista:
        for numero2 in lista2: 
            print (numero1, numero2) # O( n * m)
            conteo += 1 # O(n * m)
    return conteo
    # O(1 + 2 (n * m ) )
    # O( (n*m) )
    # big o es empleadad en ciencias de la computacion para describir la complejidad  desempemnio de un algoritmo
    

conteo = unaFuncionCualquiera(numeros,numeros2)

print( "Final:" , conteo)

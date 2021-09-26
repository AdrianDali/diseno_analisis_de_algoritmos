import time
marca1 = time.time() 

def suma(num):
    suma = 0
    for i in range(num +1 ):
        suma += i
    print(suma)


def sumaNumeros(n):
    if (n == 0):
        return 0
    else: 
        return n+sumaNumeros(n-1)    




def run():
    print("La suma es: ")
    suma(4)
    marca2 = time.time()
    print(marca2 - marca1)



if __name__ == "__main__":
    run()
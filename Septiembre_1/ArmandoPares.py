cadena1 = []
cadena2 = []
cadena3 = []

def run ():
    caracteres1 = int(input("ingresa el largo de la cadena 1: "))
    for n in range(caracteres1):
      valor = input("ingresa el valor cadena 1: ")
      print(valor)
      cadena1.append(valor)  

    caracteres2 = int(input("ingresa el largo de la cadena 2: "))
    for n in range(caracteres2):
      valor = int(input("ingresa el valor cadena 2: "))
      cadena2.append(valor) 
    
    print(cadena1)
    print(cadena2)

    for caracteres1 in cadena1:
        for caracteres2 in cadena2:
            pass 

        
if __name__ == "__main__":
    run()
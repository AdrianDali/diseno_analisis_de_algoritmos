
def numeroTelefono(numeroEntrada):
    numero = numeroEntrada
    print("#######ENTRADA################")
    numero = numero.replace(' ', '')
    if (numero[0:3] == "+52"):
        print("paso")
    else:
        
        print("##############SALIDA################")
        numero = ("+52"+numero)    
        print(numero)

def run():
    print("""

    #########TELEFONO############

    """)
    numeroTelefono("554 81216 56")
    numeroTelefono("75551234567")


    

if __name__ == "__main__":    
    run()
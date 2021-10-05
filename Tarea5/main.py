# Final
# Codigo Dali-

def calcularCambio(monto):
    billetes = [500,200,100] #O(3) O(3)
    monedas = [20,10,5,1,0.5]#O(5) O(5)
    cambioBilletes= [0,0,0]#O(3) O(3)
    cambioMonedas= [0,0,0,0,0]#O(3) O(3)

    aux = len(billetes)#O(1) O(1)
    for billete  in range(aux):#O(1) O(1)

        while (monto >= billetes[billete]):#O(4) O(4)
            monto = monto - billetes[billete]#O(1) O(1)
            cambioBilletes[billete] = cambioBilletes[billete] + 1 ;#O(3) O(3)
        print(cambioBilletes[billete], "billetes de ", billetes[billete])#O(3) O(3)
      

    aux2 = len(monedas)#O(1) O(1)
    for moneda in range(aux2):#O(1) O(1)
        while (monto >= monedas[moneda]):#O(4) O(4)
            monto = monto - monedas[moneda]#O(1) O(1)
            cambioMonedas[moneda] = cambioMonedas[moneda] + 1#O(3) O(3)
        print(cambioMonedas[moneda],"moneda de ", monedas[moneda])#O(3) O(3)
    

def run():
    monto = float(input("Cual es el monto? "))#O(1) O(1)
    calcularCambio(monto)



if __name__ == '__main__':
    run()
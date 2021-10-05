# Codigo Dali-
# Antes de reduccion 
# main.py es el final

def calcularCambio(monto):
    billetes = [500,200,100]
    monedas = [20,10,5,1,0.5]
    cambioBilletes= [0,0,0]
    cambioMonedas= [0,0,0,0,0]


    while (monto >= billetes[0]):
        monto = monto - billetes[0]
        cambioBilletes[0] = cambioBilletes[0] + 1 ;
      

    while (monto >= billetes[1]):
        monto = monto - billetes[1]
        cambioBilletes[1] = cambioBilletes[1] + 1;
     

    while (monto >= billetes[2]):
        monto = monto - billetes[2]
        cambioBilletes[2] = cambioBilletes[2] + 1;

    
    while (monto >= monedas[0]):
        monto = monto - monedas[0]
        cambioMonedas[0] = cambioMonedas[0] + 1;

    
    while (monto >= monedas[1]):
        monto = monto - monedas[1]
        cambioMonedas[1] = cambioMonedas[0] + 1;
    
    while (monto >= monedas[2]):
        monto = monto - monedas[2]
        cambioMonedas[2] = cambioMonedas[2] + 1;

    while (monto >= monedas[3]):
        monto = monto - monedas[3]
        cambioMonedas[3] = cambioMonedas[3] + 1;

    while (monto >= monedas[4]):
        monto = monto - monedas[4]
        cambioMonedas[4] = cambioMonedas[4] + 1;


    print(cambioBilletes[0], " billetes de 500")
    print(cambioBilletes[1], " billetes de 200")
    print(cambioBilletes[2], " billetes de 100")
    print(cambioMonedas[0], " moneda de 20")
    print(cambioMonedas[1], " moneda de 10")
    print(cambioMonedas[2], " moneda de 5")
    print(cambioMonedas[3], " moneda de 1")
    print(cambioMonedas[4], " moneda de 0.5")


    def run():
        monto = float(input("Cual es el monto? "))
    print(monto)
    calcularCambio(monto)



if __name__ == '__main__':
    run()


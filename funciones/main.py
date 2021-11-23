from matplotlib import pyplot

e = 2.71

# FUNCIONES CUADRATICAS.
def f1(x):
    return 2*(x**2) 
def f2(x):
    return 5*(x**2) 
def f3(x):
    return -15*(x**2)

#FUNCIONES CUBICAS 
def f4(x):
    return (x**3)
def f5(x):
    return 4*(x**3)

def f6(x):
    return 0 if x == 0.0 else 2/x

def f7(x):
    return e**x 
# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
#pyplot.plot(x, [f1(i) for i in x],label="f1")
#pyplot.plot(x, [f2(i) for i in x],label = "f2")
#pyplot.plot(x, [f3(i) for i in x],label = "f3")
#pyplot.plot(x, [f4(i) for i in x],label = "f4")
#pyplot.plot(x, [f5(i) for i in x],label = "f5")
#pyplot.plot(x, [f6(i) for i in x],label = "f6")
pyplot.plot(x, [f7(i) for i in x],label = "f7")

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
pyplot.legend()
# Mostrarlo.
pyplot.show()
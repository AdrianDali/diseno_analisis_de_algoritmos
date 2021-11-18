### DIAGRAMAS DE LINEA
import matplotlib.pyplot as plt 
#definir los datos
x1 = [3,4,5,6]
y1 = [5,6,3,4]
x2 = [2,5,8]
y2 = [3,4,3]
#Configurar las caracteristicas del grafico
plt.plot(x1,y1, label = 'Linea 1', linewidth = 4, color = 'blue')
plt.plot(x2,y2, label = 'Linea 2', linewidth = 4, color = 'green')
#Definir titulo y nombres de ejes
plt.title("Diagramas de lineas")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()
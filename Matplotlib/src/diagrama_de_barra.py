### DIAGRAMAS DE LINEA
import matplotlib.pyplot as plt 
#definir los datos
x1 = [3,4,5,6]
y1 = [5,6,3,4]
x2 = [2,5,8]
y2 = [3,4,3]
#Configurar las caracteristicas del grafico
plt.bar(x1,y1, label = 'Datos 1', width = 0.5, color = 'blue')
plt.bar(x2,y2, label = 'Datos 2', width = 0.5, color = 'green')
#Definir titulo y nombres de ejes
plt.title("Diagramas de lineas")
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda y figura
plt.legend()
plt.show()
### DIAGRAMAS DE LINEA
import matplotlib.pyplot as plt 
#definir los datos
dormir = [1,1,1,1]
comer = [1,1,1,1]
trabajar = [1,1,1]
recreacion = [1,1,1]
divisiones = [10,10,10,10]
actividades = ['Dormir','comer','trabajar','recreacion']
colores = ['red', 'purple','blue','orange']
#Configurar las caracteristicas del grafico
plt.pie(divisiones, labels=actividades , colors= colores, startangle=90,
shadow=True,explode=(0.1,0,0,0), autopct='%1.1f%%')
#Definir titulo y nombres de ejes
plt.title("grafico")

plt.show()
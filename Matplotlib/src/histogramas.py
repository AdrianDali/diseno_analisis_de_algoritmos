import matplotlib.pyplot as plt
#definir los datos
a = [22,55,62,45,21,22,34,42,42,4,42,41,5,4,8,8,43,21,235,5,8,64,100,100]

bins =[0,10,20,30,40,50,60,70,80,90,100]
#caracteristicas del grafico
plt.hist(a,bins,histtype= 'step',rwidth = 0.8,color = 'lightgreen')
#definir titulo y nombre de ejes
plt.title('Histograma')
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
#Mostrar figura
plt.show()
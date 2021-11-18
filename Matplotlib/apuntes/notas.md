#INTRODUCCION MATPLOTLIB
-libreria de trazado utilizada para graficos 2D
-tiene muchos valores predeterminados incorporados

##Apuntes
1)La figura es la ventana o pagina general en la que se dibuja todo

Puedes crear multiples figuras independientes

Una figura puede tener otras cosas, como un subtitulo, que es un titulo centrado de la figura, una leyenda, una barra de color, entre otras

2)A la figura le agregas los ejes

Los ejes es el area en la que se grafian los datos con funciones tales como plot() y scatter() y que pueden tener etiquetas asociadas 

3) Cada eje tiene un eje x y otro eje y, y cada uno de ellos contiene una numeracion.
Tambien existen las tiquetas de los ejes, el titulo y la leyenda que se deben tener en cuenta cuando se requiere personalizar los ejes, pero tambien teniendo en cuenta que las escalas de los ejes y las lineas de la cuadricula pueden ser utiles

4)Las lineas vertebrales son lineas que conectan las marcas de eje y que designan los limites del area de datos, en otras palabras, son el simplre cuadrado que puedes ver cuando has inicializado los ejes

>Los datos de machine learning para graficar en matplotlib deberan estar estructurados bajo la libreria de Numpy

#MATPLOTLIB
Todo el paquete de visualizacion de datos de Python 

#PYPLOT
Es un modulo en el paquete matplotlib. Es por eso que a mendo observamos al momento de importar la libreria matplotlib.pyplot. El modulo proporciona una interfaz que premite crear figuras y ejes de forma implicita y automatica para lograr la trama deseada

#PYLAB 
Es otro modulo que se instalal junto al paquete matplotlib. Ya no se recomienda su uso, con el uso de nuevos IDE y kernel que estan disponible en la actualidad 

> Con matplotlib podemos crear Diagramas de linea, Grafico de barras, Histograma, Grafico de dispersion, Grafico circular

##Histogramas
se usan para mostrar una distribucion son utiles cuando tenemos una matriz o lista larga

##Graficos de dispercion
se usan para comparar variables, cuando una variable se ve afectada por otra variable

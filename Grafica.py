# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
from matplotlib.patches import Polygon
#from pylab import *
import pylab
from matplotlib.ticker import MaxNLocator


def DiagramaBarras(media1,desviacion1,media2,desviacion2,media3,desviacion3,
                   media4,desviacion4,media5,desviacion5,media6,desviacion6):
    N = 5
    ind = np.arange(N)  # the x locations for the groups
    width = 0.14      # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, media1, width, color='r', yerr=desviacion1)
    rects2 = ax.bar(ind+width, media2, width, color='y', yerr=desviacion2)
    rects3= ax.bar(ind+width*2, media3,width,color='b',yerr=desviacion3)
    rects4= ax.bar(ind+width*3,media4,width,color='g',yerr=desviacion4)
    rects5=ax.bar(ind+width*4,media5,width,color='k',yerr=desviacion5)
    rects6=ax.bar(ind+width*5,media6,width,color='brown',yerr=desviacion6)

    # add some
    ax.set_ylabel('Unidades de tiempo')
    ax.set_xlabel('Numero de procesos')
    ax.set_title('Numero de Procesos vs unidades de tiempo')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('25', '50', '100', '150', '200') )
    ax.legend( (rects1[0], rects2[0],rects3[0],rects4[0],rects5[0],rects6[0]), ('Prueba1', 'Prueba2','Prueba3','Prueba4','Prueba5','Prueba6') )

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)
    autolabel(rects5)
    autolabel(rects6)

    plt.show()



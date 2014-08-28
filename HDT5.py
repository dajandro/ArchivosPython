# -*- coding: utf-8 -*-
#Universidad del Valle de Guatemala
#Pablo Diaz 13203
#Daniel Orozco 13312
#Programa que simula una CPU
#Recursos: Resource

from SimPy.Simulation import *
from random import uniform, expovariate, Random,seed
#from Grafica import * descomentar esta linea y la ultima del programa para mostrar grafica
from math import *


class Computadora(Process):
    def __init__(self,id):
        Process.__init__(self)
        self.id=id  #se le coloca un número como identidad

    def Run(self,CPU,velocidad,tiempoHold,wt):
        print "%s RAM asignada" %(self.id)
        yield hold,self,velocidad  #toma ese tiempo llegar
        self.llega = now()
        yield request,self,CPU #busca un espacio, si no hay debe hacer cola (depende de la capacidad)
        print "%5.1f %s esperando en cola" %(now(),self.id) 
        yield hold,self,tiempoHold #ocupa el parqueo el tiempo de parkTime
        tiempoTotal = now() - self.llega
        wt.observe(tiempoTotal)
        print "%5.1f %s libera RAM después de %5.1f en cola, Tiempo total=%5.1f" %(now(),self.id,tiempoHold,tiempoTotal)
        yield release,self,CPU #desocupa la cola 


class Source(Process):
    """ Source generates customers randomly"""

    def generate(self, number, interval, resource, monitor,t1):
        for i in range(number):
             cp = Computadora(id="CPU: " + str(i)+ " ")
             t = expovariate(1.0 / interval)
             activate(cp,cp.Run(CPU=resource,velocidad=t1,tiempoHold=t,wt=monitor))
             yield hold, self, now()

#---------------------------DATOS PRUEBA 1------------------------
theSeed=12345
media1=[]
desviacion1=[]
RAM=100
numeroProcesos=25 #constante
numeroCPU=1     #variable
velocidadCPU=3   #variable
intervalo=1.0   #variable
wt = Monitor()     

def model(runSeed=theSeed,procesos=numeroProcesos):                       
    seed(runSeed)
    CPU = Resource(capacity=numeroCPU,qType=FIFO)
                               
    initialize()
    s = Source('Source')
    activate(s, s.generate(number=RAM, interval=intervalo,
                          resource=CPU, monitor=wt,t1=velocidadCPU))  
    simulate(until=procesos)
    print procesos
    return (wt.mean(),sqrt(wt.var()))


#--------------------simulacion de la PRUEBA 1----------
semilla=[393939, 3155999, 777999555, 319999771,1827488282]
for Sd in semilla:
    result = model(Sd,numeroProcesos)
    if Sd==393939:
        numeroProcesos+=75
    else:
        numeroProcesos+=50
    media1.append(result[0])
    desviacion1.append(result[1])
    print("Tiempo de espera medio %6.2f unidades de tiempo con desviación estándar de %3d" % result)
    
                    
#--------------------DATOS PRUEBA 2---------------------------
theSeed=12345
media2=[]
desviacion2=[]
RAM=200            #se incrementa la memoria
numeroProcesos=25  #constante
numeroCPU=1     #variable
velocidadCPU=3   #variable
intervalo=1.0   #variable
wt = Monitor()     



#-------------------SIMULACION PRUEBA 2---------------------
semilla=[393939, 31555999, 777999555, 319999771,1827488282]
for Sd in semilla:
    result = model(Sd,numeroProcesos)
    if Sd==393939:
        numeroProcesos+=75
    else:
        numeroProcesos+=50
    media2.append(result[0])
    desviacion2.append(result[1])
    print("Tiempo de espera medio %6.2f unidades de tiempo con desviación estándar de %3d" % result)

#----------------DATOS PRUEBA 3-----------------------------
theSeed=12345
media3=[]
desviacion3=[]
RAM=100
numeroProcesos=25 
numeroCPU=1     #variable
velocidadCPU=6   #variable cambia el numero de instrucciones que ejecuta por unidad de tiempo
intervalo=1.0   #variable
wt = Monitor()     



#----------------------------SIMULACION PRUEBA 3---------------
semilla=[393939, 31555999, 777999555, 319999771,1827488282]
for Sd in semilla:
    result = model(Sd,numeroProcesos)
    if Sd==393939:
        numeroProcesos+=75
    else:
        numeroProcesos+=50
    media3.append(result[0])
    desviacion3.append(result[1])
    print("Tiempo de espera medio %6.2f unidades de tiempo con desviación estándar de %3d" % result)


#----------------DATOS PRUEBA 4-----------------------------
theSeed=12345
media4=[]
desviacion4=[]
RAM=100
numeroProcesos=25 
numeroCPU=2     #variable aumenta el numero de procesadores
velocidadCPU=3   #variable
intervalo=1.0   #variable
wt = Monitor()     



#----------------------------SIMULACION PRUEBA 4---------------
semilla=[393939, 31555999, 777999555, 319999771,1827488282]
for Sd in semilla:
    result = model(Sd,numeroProcesos)
    if Sd==393939:
        numeroProcesos+=75
    else:
        numeroProcesos+=50
    media4.append(result[0])
    desviacion4.append(result[1])
    print("Tiempo de espera medio %6.2f unidades de tiempo con desviación estándar de %3d" % result)


#--------------------------MOSTRAR RESULTADOS GRÁFICOS---------------------

#argumentos: la media y desviacion estándar de cada prueba
#no devuelve nada
#descomentar la siguiente linea para mostrar el diagrama de barras
#DiagramaBarras(media1,desviacion1,media2,desviacion2,
#               media3,desviacion3,media4,desviacion4)

                    





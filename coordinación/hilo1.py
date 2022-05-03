import threading
import time
import datetime
import logging

#Definimos dos hilos
def consultar(id_persona):
    time.sleep(2)
    return


def guardar(id_persona, data):
    time.sleep(4)
    return

tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo1", target=consultar, args=(1,))
t2 = threading.Thread(name="hilo2", target=guardar, args=(1,"Dato consultado"))

#t1.start()
#t2.start()
#Hilos sin sincronización
consultar(1) 
guardar(1, "Dato guardado")

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido " + str(tiempo_fin.second -tiempo_ini.second) +  " segundos")





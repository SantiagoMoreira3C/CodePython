import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s (%(threadName)-s) %(message)s')
#Definimos dos hilos
def consultar(id_persona):
    logging.debug("Consultado para el id " + str(id_persona))
    print('hilo 1-1')
    print('hilo 1-2')
    time.sleep(2)
    return


def guardar(id_persona, data):
    logging.info("consultado para el id " +str(id_persona) + " data: "+data)
    print('hilo 2-1')
    time.sleep(4)
    return

tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo1", target=consultar, args=(1,))
t2 = threading.Thread(name="hilo2", target=guardar, args=(1,"Dato consultado"))

#subproceso1
t1.start()
#subproceso2
t2.start()

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido " + str(tiempo_fin.second -tiempo_ini.second) +  " segundos")



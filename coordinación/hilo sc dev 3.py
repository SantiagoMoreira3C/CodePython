import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s (%(threadName)-s) %(message)s')
#Definimos dos hilos

def start_server():
  # starting server
  print("Base de datos conectada...")
  # do some startup work


def consultar(id_persona, b):
    b.wait()
    logging.debug("Consultado para el id " + str(id_persona)) 
    print('hilo 1-1')
    print('hilo 1-2')
    time.sleep(2)
    return


def guardar(id_persona, data, b):
    b.wait()
    logging.info("consultado para el id " +str(id_persona) + " data: "+data)
    print('hilo 2-1')
    time.sleep(4)
    return

tiempo_ini = datetime.datetime.now()

start_server()

b = threading.Barrier(2)

t1 = threading.Thread(name="hilo1", target=consultar, args=(1,b))
t1.start()

t2 = threading.Thread(name="hilo2", target=guardar, args=(1,"Dato consultado", b))
t2.start()
#subproceso1

#subproceso2


t1.join()
t2.join()


tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido " + str(tiempo_fin.second -tiempo_ini.second) +  " segundos")



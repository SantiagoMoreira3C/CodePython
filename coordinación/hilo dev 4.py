import threading
import time

#Tenemos un ejemplo simple en el que tenemos dos subprocesos que representan el servidor y el cliente, donde el subproceso del cliente esperará a que el servidor esté listo antes de enviarle una solicitud


def start_server():
  # starting server
  print("Iniciando servidor...")
  # do some startup work
  time.sleep(2)
  

def server(b):
    start_server()
    b.wait()
    print("Servidor listo.")

def client(b):
    print("Esperando que el servidor se prepare...")
    b.wait()
    print("Enviando solicitud al servidor...")

if __name__=='__main__':
  
  b = threading.Barrier(2, timeout=5)
  # server thread
  s = threading.Thread(target=server, args=(b,))
  s.start()
  # client thread

  c = threading.Thread(target=client, args=(b,))
  c.start()

  s.join()
  c.join()
  
  print("Conexión establecida")
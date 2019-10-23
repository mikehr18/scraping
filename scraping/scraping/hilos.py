import os
from threading import Thread
# Creando una subclase a partir de la clase "Thread"
import psycopg2

class hola_mundo(Thread):
# Método run del hilo
    def run(self):
        os.system("python hilo2.py ")

# Proceso principal
# Creando una instancia de la clase hola_mundo
hilo1 = hola_mundo()
hilo2 = hola_mundo()
hilo3 = hola_mundo()
hilo4 = hola_mundo()

# Arrancando el hilo

hilo1.start() 
hilo2.start()
hilo3.start()
hilo4.start()

# Arrancando el hilo
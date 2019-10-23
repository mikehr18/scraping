import os
from threading import Thread
# Creando una subclase a partir de la clase "Thread"
import psycopg2

class hola_mundo(Thread):
    
# Método run del hilo
    def run(self):
        os.system("scrapy crawl spiderman -a domain="+url)




try:
   connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="scrapy")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select url from link where revisada=false limit 1;"
   #select id,url from link where revisada=false order by id limit 1;

   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall() 
  

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()





url='http://likcos.blogspot.com/'

# Proceso principal
# Creando una instancia de la clase hola_mundo
hilo1 = hola_mundo()
hilo2 = hola_mundo()
hilo3 = hola_mundo()
hilo4 = hola_mundo()
hilo5 = hola_mundo()
hilo6 = hola_mundo()
hilo7 = hola_mundo()
hilo8 = hola_mundo()
hilo9 = hola_mundo()
hilo10 = hola_mundo()
hilo11 = hola_mundo()
hilo12 = hola_mundo()
hilo13 = hola_mundo()
hilo14 = hola_mundo()
hilo15 = hola_mundo()
hilo16 = hola_mundo()
# Arrancando el hilo

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()
hilo7.start()
hilo8.start()
hilo9.start()
hilo10.start()
hilo11.start()
hilo12.start()
hilo13.start()
hilo14.start()
hilo15.start()
hilo16.start()
# Arrancando el hilo
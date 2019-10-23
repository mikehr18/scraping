import os
import psycopg2
import threading

def contar(url):
    os.system("scrapy crawl spiderman -a domain="+url)



try:
   connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="scrapy")

  
   cursor = connection.cursor()

   postgreSQL_select_Query = "select url from link where revisada=false order by id limit 1;"

   for contador in range(15):
       cursor.execute(postgreSQL_select_Query)
       mobile_records = cursor.fetchall() 
       for row in mobile_records:
           url=row[0] 
           os.system("python actualizar.py "+url)
           hilo = threading.Thread(target=contar, 
                                        args=(url,)
                                        )
           hilo.start()

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
    

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()


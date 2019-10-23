import os
import psycopg2
import threading

try:
   connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="scrapy")

   
   cursor = connection.cursor()


   postgreSQL_select_Query = "select url from link where revisada=false order by id limit 1;"

   cursor.execute(postgreSQL_select_Query)
   mobile_records = cursor.fetchall()
   url='' 
   for row in mobile_records:
      url=row[0]
   os.system("scrapy crawl spiderman -a domain="+url)
   os.system("python actualizar.py "+url)
#    postgreSQL_select_Query2 = "update link set revisada=true where url=%s"
#    a=cursor.execute(postgreSQL_select_Query2,url)
#    data = "'"+str(url)+"'"
#    cursor.execute("update link set revisada=true where url={0}".format(data))


except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
    

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()


import psycopg2
import sys

try:
    connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="scrapy")

    
    cursor = connection.cursor()


    data = "'"+sys.argv[1]+"'"
    print(cursor.execute("update link set revisada=true where url={0}".format(data)))
    print("sdd url={0}".format(data))
    connection.commit()




except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
    

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()

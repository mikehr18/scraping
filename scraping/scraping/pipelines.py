# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class ScrapingPipeline(object):

    def __init__(self, db, user, passwd, host):
        self.db = db
        self.user = user
        self.passwd = passwd
        self.host = host
        
    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")
        if not db_settings: # if we don't define db config in settings
            raise 'NotConfigured' # then reaise error
        db = db_settings['db']
        user = db_settings['user']
        passwd = db_settings['passwd']
        host = db_settings['host']
        return cls(db, user, passwd, host) # returning pipeline instance


    def open_spider(self, spider):
        self.conn =psycopg2.connect(dbname=self.db,
                            user=self.user, password=self.passwd,
                            host=self.host)
        self.cursor = self.conn.cursor()
        pass

    def process_item(self, item, spider):
        try:   
            data = "'"+str(item['links'])+"'"
            sql = "INSERT INTO link (url) VALUES ('');"
            self.cursor.execute("INSERT INTO link (url) VALUES ({0});".format(data))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error :
           # print ("Error in transction Reverting all other operations of a transction ", error)
            self.conn.rollback()    
        return item



    def close_spider(self, spider):
        self.conn.close()
        pass
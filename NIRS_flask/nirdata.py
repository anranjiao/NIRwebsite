from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


class Nir(object):
    def __init__(self):#mysql登录
        self.conn = connect(
            host = MYSQL_HOST,
            port = MYSQL_PORT,
            user = MYSQL_USER,
            database = MYSQL_DATABASE,
            password = MYSQL_PASSWORD,
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor(DictCursor)  #返回json格式
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def get_customers_infos_limit(self):#读取数据库中customer信息
        sql = 'select * from customers limit 3'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            #print(temp)
            data.append(temp)
        
        return data
    
    def get_newest_costumers_8(self):
        sql = 'select * from orders order by order_date desc limit 8'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            #print(temp)
            data.append(temp)
        
        return data
    
    def get_most_products_8(self):
        sql = 'select name,quantity_in_stock from products order by quantity_in_stock limit 7;'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)
        
        return data
    
     
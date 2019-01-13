#coding:utf-8
#import pymssql
import sqlite3
import pickle
"""def connect():
  f=open("config.inf","rb")
  ip,user,psd,database_name=pickle.load(f)
  print(ip,user,psd,database_name)
  f.close()
  conn = pymssql.connect(host='127.0.0.1',
                        user='',
                        password='123',
                        database='SQLTest',
                        charset='utf8')
  #return conn
 
  cursor = conn.cursor()
  sql = 'select * from student'
  cursor.execute(sql)
    rs = cursor.fetchall()

  print(rs)
"""
def runsql(database_name,sql):

  conn = sqlite3.connect(database_name+".db")
  cursor = conn.cursor()
  cursor.execute(sql)
  # 关闭Cursor:
  cursor.close()
  # 提交事务:
  conn.commit()
  # 关闭Connection:
  conn.close()



if __name__=="__main__":
  print(eval(input()))

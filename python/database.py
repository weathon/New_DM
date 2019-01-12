#coding:utf-8
import pymssql
import pickle
def set(ip,user,psd,database_name):
  try:
    f=open("config.inf","wb")
    config=[ip,user,psd,database_name]
    pickle.dump(config,f)
    f.close()
    return 0
  except e:
    return -1,e 

def connect():
  f=open("config.inf","rb")
  ip,user,psd,database_name=pickle.load(f)
  print(ip,user,psd,database_name)
  f.close()
  conn = pymssql.connect(host='127.0.0.1',
                        user='',
                        password='123',
                        database='SQLTest',
                        charset='utf8')
  return conn
  u""" 
#查看连接是否成功
  cursor = conn.cursor()
  sql = 'select * from student'
  cursor.execute(sql)
  #用一个rs变量获取数据
  rs = cursor.fetchall()

  print(rs)
"""
if __name__=="__main__":
  print(eval(input()))

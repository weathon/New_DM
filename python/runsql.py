import sqlite3
# import pymssql
# def connect():
#   f=open("config.inf","rb")
#   ip,user,psd,database_name=pickle.load(f)
#   print(ip,user,psd,database_name)
#   f.close()
#   conn = pymssql.connect(host='127.0.0.1',
#                         user='',
#                         password='123',
#                         database='SQLTest',
#                         charset='utf8')
#   #return conn
 
# #   cursor = conn.cursor()
# #   sql = 'select * from student'
# #   cursor.execute(sql)
# #     rs = cursor.fetchall()

# #   print(rs)
# connect()
def runsql(sql):
      database_name="main"
      conn = sqlite3.connect(database_name+".db")
      cursor = conn.cursor()
      cursor.execute(sql)
      values = cursor.fetchall()
      # 关闭Cursor:
      cursor.close()
      # 提交事务:
      conn.commit()
      # 关闭Connection:
      conn.close()
      return values
#show_table
print("-----------------------------------------------")
print(runsql('select * from sqlite_master where type="table";'))
print("-----------------------------------------------")
# print(runsql(">"))
if __name__=="__main__":
    while 1:
          sqlcmd=input(">")
          if sqlcmd==":quit":
              quit()
          else:
              print(runsql(sqlcmd))
# INSERT INTO test (PATH,ID,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key12,key13,key14,key15) VALUES ("/",1551996482,"test","test","test","test","test","test","test","test","test","test","test","test","test","test","test")

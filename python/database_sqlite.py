#coding:utf-8
import sqlite3
import pickle

def runsql(sql):
      print(sql)
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

def check_dangerous(mystring):
  # sql=mystring#.lower()
  dangerous_char=["#","'","/","\\","*","(",")",'"',"<",">","=","-","%"," ","|"]
  for char in dangerous_char:
      mystring=mystring.replace(char,"&#"+str(ord(char))+";")
  # dangerous_char2=["select","union","and","or","from","form"]
  # for word in dangerous_char2:
  #   mystring.replace(word," ")#Re-write
  return mystring


# VARYING(n)
# print(runsql('''CREATE TABLE test (
# PATH nvarchar,
# ID int,
# key1 nvarchar,
# key2 nvarchar,
# key3 nvarchar,
# key4 nvarchar,
# key5 nvarchar,
# key6 nvarchar,
# key7 nvarchar,
# key8 nvarchar,
# key9 nvarchar,
# key10 nvarchar,
# key11 nvarchar,
# key12 nvarchar,
# key13 nvarchar,
# key14 nvarchar,
# key15 nvarchar
# )'''))
# if __name__=="__main__":
#   print(eval(input()))

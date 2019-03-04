import sqlite3

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
while 1:
      print(runsql(input(">")))
# INSERT INTO test (key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key1,key13,key14,key15) VALUES ("test","test","test","test","test","test","test","tst","test","test","test","test","test","test","test")
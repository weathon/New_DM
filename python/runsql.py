from database_mssql import runsql
print("-----------------------------------------------")
# print(runsql('select * from sqlite_master where type="table";'))  ONLY SQLITE
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

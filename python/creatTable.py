import database2
sqlobject=database2.MSSQL("127.0.0.1","SA","password","MAIN")
sqlobject.ExecNonQuery('''CREATE TABLE test (
 PATH nvarchar(4000),
 ID int,
 key1 nvarchar(4000),
 key2 nvarchar(4000),
 key3 nvarchar(4000),
 key4 nvarchar(4000),
 key5 nvarchar(4000),
 key6 nvarchar(4000),
 key7 nvarchar(4000),
 key8 nvarchar(4000),
 key9 nvarchar(4000),
 key10 nvarchar(4000),
 key11 nvarchar(4000),
 key12 nvarchar(4000),
 key13 nvarchar(4000),
 key14 nvarchar(4000),
 key15 nvarchar(4000)
 )''')

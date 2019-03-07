database_key=['ID','Path','key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8', 'key9', 'key10', 'key11', 'key12', 'key13', 'key14', 'key15']

def list2json(lists):
    keys=database_key
    result=[]
    lenght=len(keys)
    for i in lists:
        thisline={}
        #lists is a table
        for j in range(lenght):
            #print((i,j))
            thisline[keys[j]]=i[j]
        result.append(thisline)
    return result

def readkeys():
    f=open("key.list","r")#注意！一旦设置过keys更改可能会出错，还没有加入检测！！！
    text=f.read()
    f.close()
    return text.split("\n")#注意内容中不能有逗号
#表头数据从数据库提取？ NO!

if __name__=="__main__":
    while 1:
        print(eval(input()))
        
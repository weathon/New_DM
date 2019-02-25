def list2json(lists,keys):
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
    f=open("keys.ini","r")#注意！一旦设置过keys更改可能会出错，还没有加入检测！！！
    text=f.read()
    f.close()
    return text.split(",")#注意内容中不能有逗号
#表头数据从数据库提取？

if __name__=="__main__":
    while 1:
        print(eval(input()))
        
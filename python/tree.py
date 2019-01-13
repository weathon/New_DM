# #coding:utf-8
import database2
import os
# f=open("../config.inf")
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:            
        os.makedirs(path)
        return 0
    else:
        return -1

#Too many jumper, I am crazy!!!!
def add(father,name,dir_or_file):#Dir_or_file:if it is '1', it means user want to mk a dir, or means user want to mk a file
    if dir_or_file=="1":#dir
        mkdir("./tree"+father+"/"+name)
    else:#file
        f=open(father+"/"+name,"w")
        f.write(dir_or_file)#form name
        #mk form, write latter
        database2.runsql("create table "+name+" (id varchar(20) primary key, name varchar(20))")
        database.kmform(name=dir_or_file)
        f.close()
        

  

def read(path):
  files= os.listdir(path)#获取所有文件和文件夹
  # print files
  result=[]
  for i in files:
    if os.path.isdir(i):#如果是文件
      result.append(["file",i])#后期可能需要优化set而不是list
    else:
      result.append(["dir",i])
  return result

if __name__=="__main__":
    print(eval(input()))

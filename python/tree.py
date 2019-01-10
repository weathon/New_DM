# #coding:utf-8




import os
# f=open("../config.inf")
def add(father,name):
  dir=os.walk('..') 
  print dir


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



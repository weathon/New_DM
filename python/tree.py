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

def add(father,name,file_or_dir):
  a=file_or_dir


def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print "---  new folder...  ---"
		print "---  OK  ---"
 
	else:
		print "---  There is this folder!  ---"



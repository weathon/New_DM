﻿import eel
import os
import database2
import myjson
from tkinter import filedialog
from tkinter import *
import old_scan

@eel.expose
def getD():
    f=open("tree.json","r")
    json_data=f.read()
    f.close()
    print(json_data)
    return json_data

@eel.expose
def setTree(data):
    # print(data)
    f=open("tree.json","r")
    old_data=f.read()#For runback
    f.close()
    try:
        f=open("tree.json","w")
        f.write(data)
        f.close()
        # return 0
        returns=0
        # 5/0 Test Error
    except Exception as e:
        # return -1
        # print(repr(e))
        returns=repr(e)
        try:
            f.close()
        except:
            f=open("tree.json","w")
            f.write(old_data)#Run back
            f.close()
    return returns
#eyes tired 没能及时尝试，偷懒用data
@eel.expose
def logout():
    print("logout!")
    os._exit(0)

@eel.expose
def upload(path):
    print("Upload"+path)
    return "ff"

@eel.expose
def getkey():
    f=open("key.list","r")
    keys=f.read()
    f.close()
    return keys

# using string but not list, slow?

@eel.expose
def setkey(data):
    # print(data)
    f=open("keys.list","r")
    old_data=f.read()#For runback
    f.close()
    try:
        f=open("keys.list","w")
        f.write(data)
        f.close()
        # return 0
        returns=0
        # 5/0 Test Error
    except Exception as e:
        # return -1
        # print(repr(e))
        returns=repr(e)
        try:
            f.close()
        except:
            f=open("keys.list","w")
            f.write(old_data)#Run back
            f.close()
    return returns

@eel.expose
def welcome():
    print("Welcome")
    # For sure can open two ws://

@eel.expose
def get_cols():
    keys=myjson.readkeys()
    return keys

@eel.expose
def getData(id):
    id=database2.check_dangerous(id)
    result=database2.runsql("select * from "+id)
    # print(result)
    rmyjson=myjson.list2json(result)
    # print(rmyjson)
    return rmyjson

@eel.expose
def update(table_name,value,field,ID):
    try:
        value=database2.check_dangerous(value)
        print(value)
        database2.runsql('UPDATE %s set %s ="%s" WHERE ID=%i;' %(table_name,field,value,ID))
        myreturn="0"
    except Exception as e:
        myreturn=repr(e)

    return myreturn

@eel.expose
def chose_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

@eel.expose
def getForm():
    keys=getkey().split()
    result=""
    form="""<div class="layui-input-inline"><div class="layui-form-item" pane>
    <label class="layui-form-label">%s</label>
    <div class="layui-input-block">
    <input type="text" name="title" required lay-verify="required" placeholder="请输入对应值" autocomplete="off" class="layui-input">    
    </div>
    </div>
    </div>"""
    for i in keys:
        result+=form % i
    return result

@eel.expose
def getScaner():
    print("Getting scaner")
    try:
        mylist=old_scan.get_devices_function()
    except:
        mylist=[u"没有找到扫描仪"]
    result='<select name="scaner" lay-verify=""><option value="">请选择扫描仪</option>'
    index=0
    for i in mylist:
        result+='<option value="%i">%s</option>' %(index,i)
        index+=1
    result+="</select>"
    return result

eel.init('../html')
eel.start('index.html', options={'chromeFlags': ['--disable-http-cache','--incognito']})

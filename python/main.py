import eel
import os
import database2
import myjson

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

# @eel.expose
# def read_table(name):
#     name=str(name)
#     name=database2.check_dangerous(name)
#     mylist=database2.runsql("SELECT * FROM "+name)
#     keys=myjson.readkeys()
#     myjson_data=myjson.list2json(mylist)
#     # print(keys)
#     return_table='''<table class="layui-table" lay-data="{page:true, id:'main_table',data:'''+str(myjson_data)+''',height:315}" lay-filter="test">
#         <thead>
#             <tr>
#             <th lay-data="{field:key1,sort: true}">%s</th>
#             <th lay-data="{field:key2,sort: true}">%s</th>
#             <th lay-data="{field:key3,sort: true}">%s</th>
#             <th lay-data="{field:key4,sort: true}">%s</th>
#             <th lay-data="{field:key5,sort: true}">%s</th>
#             <th lay-data="{field:key6,sort: true}">%s</th>
#             <th lay-data="{field:key7,sort: true}">%s</th>
#             <th lay-data="{field:key8,sort: true}">%s</th>
#             <th lay-data="{field:key9,sort: true}">%s</th>
#             <th lay-data="{field:key10,sort: true}">%s</th>
#             <th lay-data="{field:key11,sort: true}">%s</th>
#             <th lay-data="{field:key12,sort: true}">%s</th>
#             <th lay-data="{field:key13,sort: true}">%s</th>
#             <th lay-data="{field:key14,sort: true}">%s</th>
#             <th lay-data="{field:key15,sort: true}">%s</th>
#             </tr>
#         </thead>
#         </table>''' % tuple(keys)
    
    
    # print(return_table)
    # return return_table

@eel.expose
def get_cols():
    keys=myjson.readkeys()
    return keys

eel.init('../html')
eel.start('index.html', options={'chromeFlags': ['--disable-http-cache','--incognito']})

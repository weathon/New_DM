import eel
import os
import database2
import myjson
from tkinter import filedialog
from tkinter import Tk
# import easygui
import old_scan
import  shutil
import base64

devlist = []
@eel.expose
def getD():
    f = open("tree.json", "rb")
    json_data = f.read().decode("utf-8")
    f.close()
    print(json_data)
    return json_data


@eel.expose
def setTree(data):
    # print(data)
    f = open("tree.json", "r")
    old_data = f.read()  # For runback
    f.close()
    try:
        f = open("tree.json", "w")
        f.write(data)
        f.close()
        # return 0
        returns = 0
        # 5/0 Test Error
    except Exception as e:
        # return -1
        # print(repr(e))
        returns = repr(e)
        try:
            f.close()
        except:
            f = open("tree.json", "w")
            f.write(old_data)  # Run back
            f.close()
    return returns
# eyes tired 没能及时尝试，偷懒用data
@eel.expose
def logout():
    print("logout!")
    os._exit(0)


# @eel.expose
# def upload(path):
#     print("Upload"+path)
#     return "ff"


@eel.expose
def getkey():
    f = open("key.list", "r")
    keys = f.read()
    f.close()
    return keys

# using string but not list, slow?


@eel.expose
def setkey(data):
    # print(data)
    f = open("key.list", "r")
    old_data = f.read()  # For runback
    f.close()
    try:
        f = open("key.list", "w")
        f.write(data)
        f.close()
        # return 0
        returns = 0
        # 5/0 Test Error
    except Exception as e:
        # return -1
        # print(repr(e))
        returns = repr(e)
        try:
            f.close()
        except:
            f = open("key.list", "w")
            f.write(old_data)  # Run back
            f.close()
    return returns


@eel.expose
def welcome():
    print("Welcome")
    # For sure can open two ws://


@eel.expose
def get_cols():
    keys = myjson.readkeys()
    return keys


@eel.expose
def getData(id):
    id = database2.check_dangerous(str(id))
    result = database2.runsql("select * from \""+id+'"')
    # print(result)
    rmyjson = myjson.list2json(result)
    # print(rmyjson)
    return rmyjson


@eel.expose
def update(table_name, value, field, ID):
    try:
        value = database2.check_dangerous(value)
        print(value)
        database2.runsql('UPDATE "%s" set %s ="%s" WHERE ID=%i;' %
                         (table_name, field, value, ID))
        myreturn = "0"
    except Exception as e:
        myreturn = repr(e)

    return myreturn


@eel.expose
def choose_folder():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    # root.lift()
    folder_selected = filedialog.askdirectory()
    # folder_selected = easygui.diropenbox()
    return folder_selected
    # bu hui zui qian tan chu, jian rong xing wen ti


@eel.expose
def getForm():
    keys = getkey().split()
    result = ""
    form = """<div class="layui-input-inline"><div class="layui-form-item" pane>
    <label class="layui-form-label">%s</label>
    <div class="layui-input-block">
    <input id=%s type="text" name="title" required lay-verify="required" placeholder="请输入对应值" autocomplete="off" class="layui-input">    
    </div>
    </div>
    </div>"""
    index = 1
    for i in keys:
        result += form % (i, "key"+str(index))
        index += 1
    return result


@eel.expose
def getScaner():
    # print("Getting scaner")
    # try:
    #     mylist=old_scan.get_devices_function()
    #     print(0)
    #     result='<select name="scaner" lay-verify=""><option value="">请选择扫描仪</option>'
    #     index=0
    #     for i in mylist:
    #         result+='<option value="%i">%s</option>' %(index,str(i))
    #         index+=1
    #     result+="</select>"
    #     print(1)
    #     return result
    # except:
    #     print(1)
    #     return '<select name="scaner" lay-verify=""><option value="">请选择扫描仪</option><option value="-1" disable>未找到扫描仪，请确保驱动安装正确</option></select>'
    pass


@eel.expose
def scan(resolution, mode, feeder, values,table_name):
    eel.PageConsole(u"扫描程序正在启动……")
    try:
        if feeder == "1":
            # feeder
            print((resolution, mode, feeder, values))
            path,myid = old_scan.feeder(resolution, mode)#id会不会重叠？
            print(path)
        else:
            # pad
            path,myid = old_scan.start(resolution, mode)
            print(path)

        for i in range(len(values)):
            values[i]=database2.check_dangerous(str(values[i]))

        table_name=str(table_name)

        format_list=[table_name,path,int(myid)]
        format_list.extend(values)#没有返回值，在原数组上面操作
        # print(format_list)
        database2.runsql('INSERT INTO "%s" \
            (PATH,ID,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key12,key13,key14,key15) \
            VALUES ("%s", %i ,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % tuple(format_list) )
        return "0"
    except Exception as e:
        return str(repr(e))


@eel.expose
def upload(path,values,table_name):
    # try:
        with open("usedid.txt","r") as f:
            #这些配置文件后期要移动到数据库
            myid=f.read()

        with open("usedid.txt","w") as f:
            f.write(str(int(myid)+1))
        # os.mkdir("./output/"+str(myid))
        # index=0
        # for name in os.listdir(path):
        #     shutil.copyfile(name,"./output/"+str(myid)+"/")
        #     index+=1
        shutil.copytree(path,"./output/"+str(myid)+"/")#最后不加一个斜杠文件名会多一个乱码字符
        path="./output/"+str(myid)+"/"
        for i in range(len(values)):
            values[i]=database2.check_dangerous(str(values[i]))

        table_name=str(table_name)

        format_list=[table_name,path,int(myid)]
        format_list.extend(values)#没有返回值，在原数组上面操作
        # print(format_list)
        database2.runsql('INSERT INTO "%s" \
            (PATH,ID,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key12,key13,key14,key15) \
            VALUES ("%s", %i ,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % tuple(format_list) )
        return "0"
    # except Exception as e:
    #     return str(repr(e))
        
#刚才搞烦了
@eel.expose
def creatTable(id):
    id=database2.check_dangerous(str(id))
    database2.runsql('''CREATE TABLE "%s" (
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
 )''' % id)

@eel.expose
def dropTable(id):
    try:
        id=database2.check_dangerous(str(id))
        print(id)
        # shutil.rmtree('./output/'+str(id))#Un-test
        folder_list=database2.runsql('SELECT * from "%s"' %id)
        for i in folder_list:
            shutil.rmtree(r'./output/'+str(i[1]))#+"/"
            # os.rmdir(r'output/'+str(i[1])+r"/")#./ or nothing?
        database2.runsql("DROP TABLE \""+str(id)+'"')#order
        myreturn="0"
    except Exception as e:
        myreturn=repr(e)
    return myreturn
    

@eel.expose
def delete(file_id,table_ID):
    file_id=database2.check_dangerous(str(file_id))
    # DELETE FROM 表名称 WHERE 列名称 = 值
    mysql='DELETE FROM "%s" WHERE "ID" = "%s"' %(table_ID,file_id)
    database2.runsql(mysql)
    shutil.rmtree(r'./output/'+file_id)#+"/"

@eel.expose
def getPicturelist(folder_id):
    print(folder_id)
    mylist=os.listdir(r'./output/'+folder_id)
    myhtml="""<br/><img onclick="details(%s)" class="list" id="img-%s" src="data:image;base64, %s" width=80%%></img><br/>"""
    result=""
    myid=0
    for i in mylist:
        with open("".join(("./output/",folder_id,"/",i)),"rb") as f:
            result+=myhtml % (myid,myid,str(base64.b64encode(f.read()),"utf-8"))
            # "".join((result,myhtml % base64.b64encode(f.read())))
        myid+=1
    return result


eel.init('./html')
eel.start('index.html', options={'chromeFlags': [
          '--disable-http-cache', '--incognito']})

import eel
import os

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

    
eel.init('../html')
eel.start('index.html', options={'chromeFlags': ['--disable-http-cache','--incognito']})

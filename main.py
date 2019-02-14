import eel


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
    try:
        f=open("tree.json","w")
        f.write(data)
        f.close()
        # return 0
        returns=0
    except:
        # return -1
        returns=-1
        #Last time
    return returns


eel.init('./')
eel.start('index.html')

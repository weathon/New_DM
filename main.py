﻿import eel


@eel.expose
def getD():
    f=open("tree.json","r")
    json_data=f.read()
    f.close()
    print(json_data)
    return json_data

@eel.expose
def setTree(data):
    print(data)


eel.init('./')
eel.start('index.html')

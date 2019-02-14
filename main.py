import eel


@eel.expose
def getD():
    return '''[{"id": 1,"label": "我的文档","children": []}]'''

eel.init('./')
eel.start('index.html')

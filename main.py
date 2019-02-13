import eel


@eel.expose
def getD():
    return '''[
                {
                    id: 1,
                    label: "",
                    children: []
                }
            ]'''

eel.init('./')
eel.start('index.html')

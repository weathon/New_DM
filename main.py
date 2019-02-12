import eel
eel.init('./')
eel.start('index.html')

@eel.expose
def helloworld(a, b):
    print(a, b, a + b)

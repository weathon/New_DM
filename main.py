import eel
eel.init('web')
eel.start('index.html')

@eel.expose
def my_python_function(a, b):
    print(a, b, a + b)
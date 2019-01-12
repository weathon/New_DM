#import database
#import pic
from flask import Flask

app= Flask(__name__)

@app.route('/')
def main():
    return "Hello World!"

@app.route('/action/connect/<ip>/<user>/<psd>/<database_name>')
def action(ip,user,psd,name):
    database.connect(ip,user,psd,name)
    

if __name__=="__main__":
    app.run(debug=True)




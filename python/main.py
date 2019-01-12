#import database
#import pic
from flask import Flask

app= Flask(__name__)

@app.route('/')
def main():
   url_for('static', filename='style.css')

@app.route('/action/connect/<ip>/<user>/<psd>/<database_name>')
def action(ip,user,psd,name):
    database.set(ip,user,psd,name)
    database.commect()
    return 0
    

if __name__=="__main__":
    app.run(debug=True)



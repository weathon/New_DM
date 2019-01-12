"""#import database
#import pic
from flask import Flask,render_template

app= Flask(__name__,static_folder="../src", template_folder="../")

@app.route('/')
def main():
    return render_template('../index.html')       



@app.route('/action/connect/<ip>/<user>/<psd>/<database_name>')
def action(ip,user,psd,name):
    database.set(ip,user,psd,name)
    database.commect()
    return 0

if __name__=="__main__":
    app.run(debug=True)
"""


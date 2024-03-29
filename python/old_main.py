
#coding=utf-8
 
from http.server import BaseHTTPRequestHandler,HTTPServer
import sys
import json
import database2 as database
import os

PORT_NUMBER = 8080
cur_dir = '../'
 
#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
 
    #Handler for the GET requests
    def do_GET(self):
        print(self.path)
        try:
            self.ar=self.path.split("?")[1]
        except:
            pass
        self.path=self.path.split("?")[0]

        run=False
        if self.path=="/":
            self.path="/index.html"
 
        try:
            #Check the file extension required and
            #set the right mime type
 
            sendReply = False 
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            elif self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            elif self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            elif self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            elif self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            elif self.path.endswith(".png"):
                mimetype="image/png"
                sendReply=True
            elif self.path.endswith(".py"):
                run=True
            elif self.path.endswith(".json"):
                mimetype="application/json"
                sendReply=True
            elif self.path.endswith(".ico"):
                mimetype="image/x-icon"
                sendReply=True
            else:
                sendReply=True
                mimetype="application/octet-stream"

           # print(self.path.split("?")[0].endswith(".json"))
                
            if sendReply == True:
                
                #Open the static file requested and send it
                f = open(cur_dir + self.path,"rb")
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            elif run:
                #print(self.path)
                if self.path=="/logout.py":
                   self.send_response(200)
                   self.send_header('Content-typr',"text/html")
                   self.end_headers()
                   self.wfile.write("<script>window.close()</script><h1>You have been logout! If this window still open, you can close it by yourself!</h1>".encode('utf-8'))
                   os._exit(0)
                else:

                    fun=self.path.lstrip("/")
                    if fun == "headers":
                        array=cut[1].split('?')
                        formname=array[0]
                        self.send_response(200)
                        self.send_header('Content-type',"application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(dict(self.headers)).encode("utf-8"))
                        #Must encode

                    elif fun=="read":
                        array=cut[1].split('?')
                        formname=array[0]
                        self.send_response(200)
                        self.send_header('Content-type',"application/json")
                        self.end_headers()
                        if database.check_dangerous(formname) == False:
                            self.wfile.write('{"message":u"DNA"}'.encode("utf-8"))
                        else:
                            self.wfile.write(json.dumps(database.runsql("select * from "+formname)).encode("utf-8"))
                        #Must encode


                    
                
            return
 
 
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
 
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)
 
    #Wait forever for incoming http requests
    server.serve_forever()
 
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()

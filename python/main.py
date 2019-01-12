
#coding=utf-8
 
from http.server import BaseHTTPRequestHandler,HTTPServer
import sys
import json

PORT_NUMBER = 8080
cur_dir = '../'
 
#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
 
    #Handler for the GET requests
    def do_GET(self):
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
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if self.path.endswith(".png"):
                mimetype="image/png"
                sendReply=True
            if "?" in self.path or self.path.endswith(".py"):
                run=True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(cur_dir + self.path,"rb")
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            elif run:
                if self.path=="/logout.py":
                   server.socket.close()
                   sys.exit()
                else:

                    cut=self.path.split("?")
                    fun=cut[0].lstrip("/")
                    if fun == "getform":
                        array=cut[1].split('?')
                        formname=array[0]
                        self.send_response(200)
                        self.send_header('Content-type',"application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(dict(self.headers)).encode("utf-8"))
                
                    
                
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

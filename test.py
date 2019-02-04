import SimpleHTTPServer
import SocketServer


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        print(self.client_address[0])
        return SimpleHTTPServer.SimpleHTTPRequestHandler.handle_one_request(self)

print("Serving local directory")
httpd = SocketServer.TCPServer(("", 8080), MyHandler)

while True:
    httpd.handle_request()
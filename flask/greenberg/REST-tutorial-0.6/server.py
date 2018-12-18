from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import cgi
import getopt, sys

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print (self.path)
        print (parse_qs(self.path[2:]))
        self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        print (form.getvalue("foo"))
        print (form.getvalue("bin"))
        self.wfile.write("<html><body><h1>POST Request Received!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=GP, host='localhost', port=8088):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    #print ('Server running at localhost:8088...')
    print('Server running at {}:{}'.format(host,port))
    #print ('Server running at {}:{}...').format(host,port)
    httpd.serve_forever()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    host='127.0.0.1'
    port='5000'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["host", "port"])
        print("no error")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) 
    for o,a in opts:
        if o in ('-p', '-port'):
            port = a
        elif o in ('-h', '-host'):
            host = a
    run(port=int(port))

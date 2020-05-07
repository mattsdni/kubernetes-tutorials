from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
from datetime import datetime as d

requests = 0
host = socket.gethostname()
ip = socket.gethostbyname(host)
start_time = d.now()


class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global requests
        requests += 1
        self.send_response(200)
        self.send_header("Content - type", "text/plain")
        self.end_headers()
        content = bytes(f"Hello from Kubernetes! Running on {host}\n", "UTF-8")
        self.wfile.write(content)
        print(f"Running On: {ip} | Total Requests: {requests} | App Uptime: {(d.now() - start_time).seconds} seconds | Log Time: {d.now()}")


if __name__ == '__main__':
    httpd = HTTPServer((host, 8000), WebServer)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

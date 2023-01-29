import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        slog = open('data/syslog.log', 'a+')
        slog.write(self.request[0].decode("utf-8") + "\n")
        slog.close()

with socketserver.UDPServer(('0.0.0.0', 514), MyUDPHandler) as server:
    server.serve_forever()
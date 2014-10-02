import socketserver
import threading


class ThreadedRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), "ascii")
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), "ascii")
        print(data)
        self.request.sendall(response)


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    PORT = 4711
    server = ThreadedServer(("localhost", PORT), ThreadedRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = False
    server_thread.start()
    print("server is now running on port {}".format(PORT))

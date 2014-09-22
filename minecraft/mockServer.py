import socket
import socketserver
import threading

class ThreadedRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), "ascii")
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), "ascii")
        self.request.sendall(response)

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
"""
    def __init__(self, address="localhost", port=4711):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((address, port))
        self.socket.listen(1) #TODO: see if wee need a bigger queue


    def run(self):
        while True:
            conn, addr = self.socket.accept()
            data = conn.recv(1024)
            """


if __name__ == "__main__":
    PORT = 4711
    server = ThreadedServer(("localhost", PORT), ThreadedRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = False
    server_thread.start()
    print("server is now runnin gon port {}".format(PORT))
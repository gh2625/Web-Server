# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()   # accepting connections

        try:
            message = connectionSocket.recv(1024).decode()   # receive client message
            filename = message.split()[1]

            # Open the requested file (read as bytes)
            f = open(filename[1:], "rb")

            # HTTP response header for a valid request
            header = b"HTTP/1.1 200 OK\r\n"
            header += b"Server: SimplePythonServer\r\n"
            header += b"Content-Type: text/html; charset=UTF-8\r\n"
            header += b"\r\n"   # blank line ends the header

            # Read file contents
            filedata = f.read()
            f.close()

            # Send headers + file content in ONE send call
            connectionSocket.sendall(header + filedata)

            connectionSocket.close()

        except Exception as e:
            # Send 404 Not Found response
            header = b"HTTP/1.1 404 Not Found\r\n"
            header += b"Server: SimplePythonServer\r\n"
            header += b"Content-Type: text/html; charset=UTF-8\r\n"
            header += b"\r\n"

            body = b"<html><body><h1>404 Not Found</h1></body></html>"

            connectionSocket.sendall(header + body)

            # Close client socket
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)
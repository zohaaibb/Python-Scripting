import socket
import threading

def handle_client(conn, addr):
    print(f"+ New connection {addr}")

    try:
        data = conn.recv(1024)
        print(f"The data received is {data.decode()}")

        conn.send(b" Hello from Server")

    except Exception as e:
        print(f"Error with {addr}")
    finally:
        conn.close()
        print(f"[=] connection closed {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))

    server.listen(6)
    print(" Server is Listening ......")
    while True:
        conn, addr = server.accept()
        print(f"The Client connected {addr}")
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
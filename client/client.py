import socket

def run_client(server_host='localhost', server_port=9090):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")
        while True:
            msg = input("Please write your message: ")
            sock.sendall(msg.encode())
            print(f"Sent data to server: {msg}")

            data = sock.recv(1024)
            print(f"Received data from server: {data.decode()}")

if __name__ == "__main__":
    run_client()

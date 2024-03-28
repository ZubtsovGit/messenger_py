from auth import get_client_name, save_client_name
from validator import get_valid_port

import socket
import logging

HOST: str = 'localhost'
PORT: int = get_valid_port(input("Введите номер порта [9090]: "))

# Настройка логгера
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        logging.info(f"Сервер запущен и слушает {HOST}:{PORT}")

        try:
            while True:
                logging.info("Ждём соединений...")
                conn, addr = sock.accept()
                logging.info(f"Клиент подключен: {addr}")
                with conn:
                    try:
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            received_msg = data.decode()
                            logging.info(f"Received data from client: {received_msg}")
                            conn.sendall(data)
                            logging.info(f"Sent data back to client: {received_msg}")
                            if received_msg == 'exit': 
                                break
                    finally:
                        conn.close()  
                        logging.info("Клиент отключен")
        except KeyboardInterrupt:
            logging.info("Сервер остановлен вручную")
        
        finally:
            sock.close()  

if __name__ == "__main__":
    run_server()





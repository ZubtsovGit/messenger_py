import logging
import socket

def get_valid_port(starting_port: str):
    try:
        port = int(starting_port)
        assert 0 <= port <= 65535
    except (ValueError, AssertionError):
        logging.warning("Некорректный номер порта. Используется значение по умолчанию: 9090.")
        port = 9090

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as temp_sock:
            try:
                temp_sock.bind(('', port))
                # Порт свободен, выводим номер порта в консоль
                print(f"Сервер слушает порт {port}")
                return port
            except OSError as e:
                if e.errno == 98 or e.errno == 10048:  # Номер ошибки для занятого порта в Linux и Windows
                    logging.warning(f"Порт {port} занят, пробуем порт {port + 1}")
                    port += 1
                else:
                    raise e
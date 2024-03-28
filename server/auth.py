def get_client_name(client_ip):
    """Получить имя клиента по его IP-адресу."""
    try:
        with open('clients.txt', 'r') as file:
            for line in file:
                ip, name = line.strip().split(',')
                if ip == client_ip:
                    return name
    except FileNotFoundError:
        pass  # Файл с клиентами еще не создан
    return None

def save_client_name(client_ip, client_name):
    """Сохранить имя клиента и его IP-адрес."""
    with open('clients.txt', 'a') as file:
        file.write(f'{client_ip},{client_name}\n')
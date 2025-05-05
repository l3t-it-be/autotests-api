import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        client_socket.connect(server_address)
        print('Подключено к серверу. Введите сообщение (или "exit" для выхода):')

        while True:
            message = input('> ')
            if message.lower() == 'exit':
                break

            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print('Ответ от сервера:\n', response)
    except Exception as e:
        print(f'Ошибка: {e}')
    finally:
        client_socket.close()

if __name__ == '__main__':
    run_client()
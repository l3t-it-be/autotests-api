import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print(f'Сервер запущен и ждет подключений на {server_address[0]}:{server_address[1]}')

    messages_history = []

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f'Пользователь с адресом: {client_address} подключился к серверу')

            try:
                while True:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        break

                    print(f'Пользователь с адресом: {client_address} отправил сообщение: {data}')
                    messages_history.append(data)

                    if len(messages_history) == 1:
                        response = messages_history[0]
                    else:
                        response = '\n'.join(messages_history)

                    client_socket.send(response.encode())
            finally:
                client_socket.close()

    except KeyboardInterrupt:
        print('Сервер завершает работу...')
    finally:
        server_socket.close()

if __name__ == '__main__':
    run_server()

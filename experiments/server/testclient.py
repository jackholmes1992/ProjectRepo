if __name__ == '__main__':
    import socket

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 44444))

    # Send the data
    message = b'Hello, world'
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    # Receive a response
    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    s.close()

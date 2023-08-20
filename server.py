import socket
def decrypt(text):
    # Decrypts a message using the Caesar Cipher.
    shift = 4
    result = ""
    for char in text:
        if char.isalnum():
            if char.isnumeric():
                char_code = (int(char) - shift) % 10
                result += str(char_code)
            elif char.isupper():
                char_code = (ord(char) - shift - 65) % 26 + 65
                result += chr(char_code)
            else:
                char_code = (ord(char) - shift - 97) % 26 + 97
                result += chr(char_code)
        else:
            result += char
    return result
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.17.161', 8888))
server_socket.listen(1)

print('Server listening on port 8888...')
terminate = False
while terminate==False:
    client_socket, address = server_socket.accept()
    print(f'Connection established from {address}\n')

    data = client_socket.recv(1024).decode('utf-8')
    messsage = decrypt(data)
    print(f'\nReceived message from client: {messsage}\n\n')

    # send a response back to the client
    response = 'Message received'
    client_socket.send(response.encode('utf-8'))

    ter = client_socket.recv(1024).decode('utf-8')
    if ter=='y' :
        terminate = True

    client_socket.close()

import socket
def encrypt(text):
    # Encrypts a message using the Caesar Cipher.
    shift = 4
    result = ""
    for char in text:
        if char.isalnum():
            if char.isnumeric():
                char_code = (int(char) + shift) % 10
                result += str(char_code)
            elif char.isupper():
                char_code = (ord(char) + shift - 65) % 26 + 65
                result += chr(char_code)
            else:
                char_code = (ord(char) + shift - 97) % 26 + 97
                result += chr(char_code)
        else:
            result += char
    return result

choice = True
while choice==True :
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.17.161', 8888))

    message = input("Enter the message u want to send : ")
    result = encrypt(message)
    print("\nencrypted message is : ",result)
    client_socket.send(result.encode('utf-8'))

    # receive response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print("\nReceived response from server: ",response)
    print("..........................")
    cont = input("Do you want to send another message (yes-y)/(no-n) : ")
    if cont=='y':
        choice=True
    else :
        choice=False
        ter = 'y'
        client_socket.send(ter.encode('utf-8'))
    
        
client_socket.close()





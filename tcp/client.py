from socket import *
serverName = '10.0.0.218'
serverPort = 27001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024).decode("utf-8")
print 'From Server:', modifiedSentence
clientSocket.close()

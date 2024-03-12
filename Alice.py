#Alice Side

#colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Have to install rsa module if not already available
import rsa
import socket
import pickle

HOST = ''

#Port Setting
PORT = 3000
print("Port: ",PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
(alice_pub, alice_priv) = rsa.newkeys(1024)

while True:
    print(bcolors.HEADER,"Establising Connection : ",bcolors.ENDC)
    clientSocket, address = s.accept()
    frombob = ""
    print(bcolors.OKBLUE,"Successfully Established Connection\n",bcolors.ENDC)
    
    while True:
        bobPubPick= clientSocket.recv(4096)
        if not bobPubPick:
            break
        #Alice Public key to confirm it doesnt change for the session
        print(bcolors.OKCYAN,alice_pub ,bcolors.ENDC,"\n")
        #We unpickle Bob public key
        bob_pub = pickle.loads(bobPubPick)
        #Alice can send message and we encrypt it
        aliceMsg = input("Send a message to Bob : \n")
        #variable-width character encoding used for electronic communication
        aliceMsg = aliceMsg.encode("utf-8")
        #Alice sends the message to BOB using his public key
        aliceCipher = rsa.encrypt(aliceMsg, bob_pub)
        #Create a list for the cipher and alice pub key
        list_send = [aliceCipher, alice_pub]
        #we convert the list into bytes inorder to send the message
        pickleList = pickle.dumps(list_send)
        print(bcolors.OKBLUE,"\nMessage successfully sent to Bob \n",bcolors.ENDC)
        clientSocket.send(pickleList)
        #Receiving BOB message in CIPHER TEXT AND DECRYTPING IT
        bobData = clientSocket.recv(4096)
        if not bobData:
            break
        #unpickle Cipher
        bobData = pickle.loads(bobData)
        print("The CipherText received by Bob is : \n" ,bcolors.OKGREEN, str(bobData),bcolors.ENDC )
     
        #Decryption of the cipher into normal form
        print("The Deciphered text from Bob Ciphertext is : ")
        bobText = rsa.decrypt(bobData, alice_priv)
        print(bcolors.OKGREEN,bobText.decode("utf-8"),bcolors.ENDC,"\n")


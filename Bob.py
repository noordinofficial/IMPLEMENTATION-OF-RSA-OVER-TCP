#Bob Side

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
import socket
import rsa
import pickle

# Servers ip address
HOST=socket.gethostname()

#Server setting
PORT = 3000
print("Port: ",PORT)
print(bcolors.HEADER,"Establising Connection : ",bcolors.ENDC)
print(bcolors.OKBLUE +"Successfully Established Connection\n"+bcolors.ENDC)

#Generating keys
(bob_pub, bob_priv) = rsa.newkeys(1024)

#Pickling 
bobPubPick = pickle.dumps(bob_pub)

#Creating a socket connection

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
     #Bob Public key to confirm it doesnt change for the session
     print(bcolors.OKCYAN,bob_pub,bcolors.ENDC,"\n")
     #Connecting to the port numbers
     sock.connect((HOST, PORT))
     sock.send(bobPubPick)
     #Waiting and pub_key
     print("Waiting for Alice CipherText \n")
     #Unpickle bob data
     alice_Data = sock.recv(3000) ##bytes
     unpickalice_Data = pickle.loads(alice_Data)
     cipher = unpickalice_Data[0]
     alice_pub = unpickalice_Data[1]
     #We decrypt it using BOB private key
     print("The CipherText received by Alice is : \n" ,bcolors.OKGREEN, str(cipher),bcolors.ENDC)
     print("The Deciphered text from Alice Ciphertext is : \n")
     decipher = rsa.decrypt(cipher, bob_priv)
     print(bcolors.OKGREEN,decipher.decode("utf-8"),bcolors.ENDC,"\n")
     #user message input for BOB
     bobMsg=input("Send a message to Alice : \n")
     #cipher with bob_pub as Received
     bobMsg = bobMsg.encode("utf-8")
     bobCipher = rsa.encrypt(bobMsg , alice_pub)
     #pickle the Cipher for sending
     bobCipherPick = pickle.dumps(bobCipher)
     sock.send(bobCipherPick)
     print(bcolors.OKBLUE,"Message successfully sent to Alice \n",bcolors.ENDC)


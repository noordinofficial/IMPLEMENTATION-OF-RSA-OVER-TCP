# IMPLEMENTATION-OF-RSA-OVER-TCP
A)	Introduction 
RSA (Rivest-Shamir-Adleman) is a popular asymmetric cryptographic technique that Ron Rivest, Adi Shamir, and Leonard Adleman initially introduced in 1977. The security of the RSA method is predicated on the mathematical challenge of factoring big numbers into their prime factors. It is frequently used for encrypted sensitive data storage, digital signatures, and secure communication. The RSA algorithm, which bears the names of its creators, is regarded as one of the most widely used and secure public-key cryptography methods in use at the moment. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private Key is kept private.
An example of asymmetric cryptography:
1.	A client (for example browser) sends its public key to the server and requests for some data.
2.	The server encrypts the data using client’s public key and sends the encrypted data.
3.	Client receives this data and decrypts it.
Since this is asymmetric, nobody else except browser can decrypt the data even if a third party has public key of browser.
B)	Methodology
In this project we wrote a program to implement RSA algorithm with key size 1024 bits using the Python language chosen due to the ease of access of python and its libraries which are free and easier to use. The key size of 1024 bits was used to store and determine the size of the key. After the generation of public key and private key using the random numbers generated to create the RSA algorithm, we used the key to send message between Alice and Bob to demonstrate encryption and decryption process. Two separate programs were written for Alice and Bob in order for them to communicate in a secure and encrypted method using the TCP communication protocol. 
C)	Requirements 
The project requirements for this section include the use of the Python IDE and a python library called the RSA module, which can be installed by performing a pip install RSA module.

D)	System Implementation 
This section shows how the RSA encryption and decryption was implemented in both the Alice and Bob application. Below attached are the python codes that implement the system required. 
![Uploading image.png…]()

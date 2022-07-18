# encryptionmicroservice

HOW TO REQUEST ENCRYPTION/DECRYPTION FROM MICROSERVICE

This microservice uses text files for communication. In order to request encryption/decryption, the instructions for the microservice must be written in the 'pw.txt' file.  The template for the instructions is as follows:

Line 1: 'e' or 'd' (to denote encryption or decryption)

Line 2: path to 'hashholder.txt' (the path for the holding file for the microservice)
          NOTE: This must be the local path for the microservice, not the path for the main application; is almost always 'hashholder.txt'
          
Line 3: encryption key (FOR DECRYPTION ONLY)

Therefore, a sample call for the microservice for encryption is:

    f = open("/path/to/pw.txt", "w")
    
    f.write("e\nhashholder.txt")

Similarly, a sample call to the microservice for decryption is:

    f = open("/path/to/pw.txt", "w")
    
    f.write("d\nhashholder.txt\n" + key) 
        # key is the encryption key used to decrypt the file
        
NOTE: For encryption, hashholder.txt must be populated with the contents to be encrypted before the call is made. For decryption, hashholder.txt must be      populated with the contents to be decrypted.


HOW TO RECEIVE DATA FROM MICROSERVICE

For the encryption, the encrypted file is made available for the user to save to their local machine. The encrypted key is then displayed via a popup message.  The encrypted file is also found in the hashholder.txt file.

For the decryption, the decrypted file is made available to the client service via the hashholder.txt file. Upon decryption, the decrypted file is held in the hashholder.txt file, allowing the client service to access this unencrypted file to do whatever sorts of data manipulation needs to be done.


UML Diagrams

To Encrypt a File

![Sequence Diagram ATM Transferal](https://user-images.githubusercontent.com/91216579/179605202-b806936e-bc25-46bc-9c4a-2562655215ce.png)

To Decrypt a File

![Sequence Diagram ATM Transferal(1)](https://user-images.githubusercontent.com/91216579/179605241-bc6305c0-0b1c-4951-9592-733d7013de1c.png)

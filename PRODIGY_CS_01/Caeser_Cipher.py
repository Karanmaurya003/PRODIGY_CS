letters = 'abcdefghijklmnopqrstuvwxyz'
def encrypt_decrypt(letters):
    print("Do you want to encrypt or decrypt? ")
    choice = input("e/d").lower()
    #Encrypt Message
    if choice == 'e':
        cyphertext = ''
        text = input("\n Enter the message: ").lower()
        key = int(input("\n Enter the key: "))
        for letter in text:
            if letter != ' ':
                pos = letters.find(letter)
                if pos != -1:
                    cyphertext += letters[(pos + key)% 26]
                else:
                    cyphertext += letter   #preserving special charactes and numbers
            else: 
                cyphertext += ' '           #preserving space 
        print('\nEncrypted Message: ',cyphertext)
        
        print("\n Encryption Done Successfully :)")

    #Decrypt Message
    elif choice == 'd':
        plaintext = ""
        cyphertext = input("\n Enter the Cypher Text: ").lower()
        key = int(input("\n Enter the key: "))
        for letter in cyphertext:
            if letter != ' ':
                pos = letters.find(letter)
                if pos != -1:
                    plaintext += letters[(pos - key)% 26] 
                else:
                    plaintext += letter      #preserving special characters and numbers
            else:
                plaintext += ' '             #preserving space
        print('\nDecrypted Message: ', plaintext)
        print("Decryption Done Successfully :)")    
    else:
        print("\nExiting Program...")   
        return          
print("\n Caeser Cipher Algorithm")
encrypt_decrypt(letters)








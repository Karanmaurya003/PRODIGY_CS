from PIL import Image
import os

#Encrypt-Decrypt image function
def encrypt_decrypt_image(key,choice):
    try:
        #open the file
        image_path = input("\nEnter the path of the image to be encrypted/decrypted (eg., 'image.png' , 'image.jpg'): ")
        print("\nsuccess 1")
        image_path = image_path.strip('"')
        image_path = image_path.replace("//","/")
        image_path = r"{}".format(image_path)
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size
        
        for x in range(width):
            for y in range(height):
                r,g,b = pixels[x,y]              #Extracting the pixels RGB value
                #Logic for encrypting image
                if choice == 1:
                    r = (r + key) % 256
                    g = (g + key) % 256
                    b = (b + key) % 256        
                #Logic for decrypting image
                else:
                    r = (r - key) % 256
                    g = (g - key) % 256
                    b = (b - key) % 256
                pixels[x,y] = r,g,b              # Reassigning the pixels new RGB value
                    
        #saving the file as _encrypted.png/_decrypted.png
        if choice == 1:
            encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypted.png"
            image.save(encrypted_image_path)
            print(f"\nImage Encrypted Succesfully\n Check file: {encrypted_image_path}")
        else:
            decrypted_image_path = os.path.splitext(image_path)[0] + "_decrypted.png"
            image.save(decrypted_image_path)
            print(f"\nImage Decrypted Succesfully\n Check file: {decrypted_image_path}")
    #Handling Errors
    except OSError:
        print("\nUnsupported image format. Use valid image format (jpg,png)")
    except FileNotFoundError:
        print("\nImage not found. Check path and try again")
    except Exception as e:
        print(f"\nError Manipulating Image: {e}")
    
#define main function
def main():
    print("\nImage Pixel Manipulation Tool")
    key = int(input("\nEnter the key to encrypt/decrypt: "))
    print("\nWhat do you want to do ;)\n 1. Encrypt the Image \n 2. Decrypt the Image")
    choice = int(input("\n Choose (1/2) :"))
    if choice in [1,2]:
        encrypt_decrypt_image(key,choice)
    else:
        print("\nInvalid Choice")
        print("\nExiting the program...")

#entry point of the script
if __name__ == "__main__":
    main()

                


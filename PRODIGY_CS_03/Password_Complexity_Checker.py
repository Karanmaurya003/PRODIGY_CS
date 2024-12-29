import math

#define the calcuate entropy funtion
def calculate_entropy(password):
    length = len(password)       #password length
    char_set = 0
    if any(c.islower() for c in password):
        char_set += 26           #for lowercase letters
    if any(c.isupper() for c in password):
        char_set += 26           #for uppercase letters
    if any(c.isdigit() for c in password):
        char_set += 10           #for digits
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
        char_set += 32           #for special character
    if char_set == 0:            #handling if none of the case matches
        return
    
    #calculating the entropy
    entropy = int(length * math.log2(char_set))
    return entropy

#Giving password feedback as per the NIST password selection criteria
def password_feedback(password):
    entropy = calculate_entropy(password)
    if len(password) < 8:        #NIST password length criteria
        return "Too Weak, :( increase the strength of your password"
    
    #NIST password entropy criteria
    elif (entropy < 28):        
        return "Easily guessable, Password is too simple. Use a mix of letters, numbers, and symbols."
    elif (28 <= entropy < 35):
        return "Fair (susceptible to targeted attacks), try increasing the complexity and length of password"
    elif (36 <= entropy < 59):
        return "Strong password (resistant to common attacks)"
    else:
        return "Very strong password (highly secure)"
    
#Starting Point
if __name__ == "__main__":
    print("PASSWORD COMPLEXITY CHECKER")
    print("---------------------------")
    password = input("Enter password to check: ")
    feedback = password_feedback(password)
    print(feedback)
    print(calculate_entropy(password))


    

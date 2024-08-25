import random 
import string

def password_generator(length):
    if length<4:
        raise Exception("Your Password length should be at least 4.")
    special_char = "@#%$&*/|.!^+-[]_;:<>?"
    my_characters = string.ascii_letters + string.digits + special_char
    my_password = random.sample(my_characters, length)
    return ''.join(my_password)
    
try:
    length=int(input("Enter the Length of your Password : "))
    print("Generated Password is : ",password_generator(length))
except Exception as exc:
    print(f"{exc}")

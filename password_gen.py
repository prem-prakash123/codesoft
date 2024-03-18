import string
import random
if __name__ == "__main__":
 pas= string.ascii_letters + string.digits + string.punctuation
 password_length= int(input("Enter password length:-"))
 gen= "".join(random.choice(pas) for i in range(password_length))
 print("Your password is:\n", gen)

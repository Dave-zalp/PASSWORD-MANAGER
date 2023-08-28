import  random
import string
import time

def GenPass(lenght=None):
    new_pass = ""
    if lenght is None:
        lenght == 8
    words = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    while len(new_pass) != lenght:
            new_pass += random.choice(words)
    return new_pass


long = int(input("Enter Length of the desired password: "))
print(f"Generating Password of length {long}....")
time.sleep(3)
print(f"New Password is {GenPass(long)}")


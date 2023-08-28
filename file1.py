import hashlib

def hashVal(password):
    Enc0d3d = password.encode('UTF-8')  #encodedes the password in 'utf-8 encoding'

    hash_obj = hashlib.sha256(Enc0d3d)  #The hashing object

    digest = hash_obj.hexdigest()

    return digest

val = input("Enter your password: ")

val2 = hashVal(val)

stmt = print(f"The sha-256 hashed Value of {val} is {val2}")



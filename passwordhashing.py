# Demo of secret hashing
import hashlib, binascii, os

def menu():
    print("\n"*50)
    print("What do you want to do?")
    print("1. Encrypt something")
    print("2. Check something")
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("> ")
    return choice


def hash_password():
    password = input("What is the password to hash?")
    """Hash a password for storing."""
    # generate 60 random bytes, pass them through the hashlib and turn into hex characters
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii') 
    # use a different hashing algorithm which uses this salt to add extra randomness
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),  
                                  salt, 100000)
    # turn this new hash into hex characters
    pwdhash = binascii.hexlify(pwdhash)
    # make a new hash string containing the salt (first 64 characters) and the hash itself
    print("copy this:\n")
    print((salt + pwdhash).decode('ascii'))
    print()

def verify_password():
    stored_password = input("What is the stored password hash?")
    provided_password = input("What is your password guess?")
    
    """Verify a stored password against one provided by user"""
    # grab the first 64 characters of the hash, which is actually the salt
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    # run the new password  uess through the hashing algorithm with the same salt
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    # turn it into text
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    if pwdhash == stored_password:
        print("\n\nThat's right!")
    else:
        print("\n\nGuess again")

while True:
    choice = menu()
    if choice == "1":
        hash_password()
    else:
        verify_password()

    input("Press Enter to continue")

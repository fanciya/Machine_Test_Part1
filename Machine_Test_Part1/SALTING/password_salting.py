import bcrypt

def generate_salt():
    return bcrypt.gensalt()

def hash_password(password, salt):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

def main():
    # Get a password from the user
    password = input("Enter your password: ")

    # Generate a random salt
    salt = generate_salt()

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    print(f"Password: {password}")
    print(f"Salt: {salt}")
    print(f"Hashed Password: {hashed_password}")

    # Check a password against the stored hash
    input_password = input("Enter the password again for verification: ")

    if check_password(input_password, hashed_password):
        print("Password is correct.")
    else:
        print("Password is incorrect.")

if __name__ == "__main__":
    main()

def get_password():
    password = input("Enter a password (minimum {} characters): ".format(MINIMUM_PASSWORD_LENGTH))
    while len(password) != MINIMUM_PASSWORD_LENGTH:
         if len(password) >= MINIMUM_PASSWORD_LENGTH:
            return password
         else:
            print("Password must be at least {} characters long. Try again.".format(MINIMUM_PASSWORD_LENGTH))

         password = input("Enter a password (minimum {} characters): ".format(MINIMUM_PASSWORD_LENGTH))

username = "Wanji"
password = "password"

username_input = input ("username: ")
password_input = input ("password: ")

if username_input == username and password_input:
    print("Access granted")
elif username_input == username and password_input != password:
    print("password incorrect")
elif username_input != username and password_input == password:
    print("username incorrect")
else:
    print("You might want to check both fields")
    




username = input("Enter username")
password = input("Enter password")

if username == "student":
    if password == "abcd1234":
        print("Logged in")
    else:
        print("incorrect password")
else:
    print("incorrect username")
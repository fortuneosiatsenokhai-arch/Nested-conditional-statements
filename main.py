user_name=input("Enter user name: ")
password=input("Enter password: ")

if user_name=="Penguin":
    if password=="12345":
        print(f"Welcome back {user_name}")
    else:
        print("password incorrect!!")
else:
    print("Username incorrect!!")
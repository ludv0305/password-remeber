import json

choice1 = input("do you want to sign in or sign up? ").lower()

if choice1 == "sign in":
    username = open("login.json", "r")
    users = username.read()
    ask = input("what is your username? ")
    if ask == users:
        print("velcome")
        choice2 = input("do you want to find a old password or enter a new one? ")
        if choice2 == "enter" or choice2 == "enter a new one" or choice2 == "new one" or choice2 == "a new one":
            new_file = input("what do you want to be the name of your file? (remeber to put .json at the end) ")
            new_password = input("what is the username and password? ")
            dump2 = json.dumps(new_password)
            with open(new_file, "w") as nf:
                nf.write(new_password)
        elif choice2 == "find" or choice2 == "find an old file" or choice2 == "find an old password" or choice2 == "old password":
            which = input("what is the name of the file the password is stored in? ")
            find = open(which, "r")
            passwords = find.read()
            print(passwords)
    elif ask != users:
        print("wrong password")
elif choice1 == "sign up":
    new = input("what should your username be? ")
    dump = json.dumps(new)
    with open("login.json", "w") as f:
        f.write(dump)
    print("thanks for signin up:)")
    print("run the program again to do more")

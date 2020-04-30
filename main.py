import json

valg1 = input("vil du logge ind eller oprette en bruger? ").lower()

if valg1 == "loge ind" or valg1 == "loge på" or valg1 == "log på" or valg1 == "log ind":
    username = open("login.json", "r")
    users = username.read()
    ask = input("hvad er dit brugernavn? ")
    if ask == users:
        print("velkommen")

elif valg1 == "oprette ny" or valg1 == "oprette en bruger" or valg1 == "oprette en ny bruger":
    new = input("hvad skal dit brugernavn være? ")
    dump = json.dumps(new)
    with open("login.json", "w") as f:
        f.write(dump)
    print("tak fordi du tilmeldte dig:)")


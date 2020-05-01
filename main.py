import json

valg1 = input("vil du logge ind eller oprette en bruger? ").lower()

if valg1 == "loge ind" or valg1 == "loge på" or valg1 == "log på" or valg1 == "log ind":
    username = open("login.json", "r")
    users = username.read()
    ask = input("hvad er dit brugernavn? ")
    if ask == users:
        print("velkommen")
        valg2 = input("vil du finde et gammelt password eller indtaste et nyt? ")
        if valg2 == "ny" or valg2 == "nyt" or valg2 == "indtaste et nyt" or valg2 == "en ny" or valg2 == "et nyt":
            new_file = input("hvad skal filen hedde? (husk at afslutte med .json) ")
            new_password = input("hvad er brugernavnet og passwordet? ")
            dump2 = json.dumps(new_password)
            with open(new_file, "w") as nf:
                nf.write(new_password)
        elif valg2 == "finde" or valg2 == "finde et gammelt" or valg2 == "finde et gammelt password":
            hvilket = input("hvad hedder filen som passwordet er gemt i")
            find = open(hvilket, "r")
            passwords = find.read()
            print(passwords)
elif valg1 == "oprette ny" or valg1 == "oprette en bruger" or valg1 == "oprette en ny bruger":
    new = input("hvad skal dit brugernavn være? ")
    dump = json.dumps(new)
    with open("login.json", "w") as f:
        f.write(dump)
    print("tak fordi du tilmeldte dig:)")
    print("kør programmet igen for at gøre noget mere")


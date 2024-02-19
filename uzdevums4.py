def lasit_failu(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            saturs = fails.read()
        print("Faila saturs:")
        print(saturs)
    except FileNotFoundError:
        print("Kļūda: fails '{}' nav atrasts.".format(nosaukums))
    except Exception as e:

        print("Kļūda: {}".format(e))


if __name__ == "__main__":
    nosaukums = input("Ievadiet faila nosaukumu: ")
    formāts = input("Ievadiet faila formātu (paplašinājumu): ")

    faila_nosaukums = "{}.{}".format(nosaukums, formāts)

    lasit_failu(faila_nosaukums)

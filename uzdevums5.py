def ierakstit_faila(vards, fails):
    try:
        with open(fails, 'w') as f:
            f.write(vards)
        print("Vārds veiksmīgi ierakstīts failā '{}'.".format(fails))
    except IOError:
        print("Kļūda: Nevarēja pierakstīt failā '{}'.".format(fails))
    except Exception as e:
        print("Kļūda: {}".format(e))


if __name__ == "__main__":
    vards = input("Ievadiet savu vārdu: ")
    fails = "lietotajs.txt"

    ierakstit_faila(vards, fails)
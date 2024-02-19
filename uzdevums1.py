def lasit_un_drukat(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_key:
            saturs = faila_key.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")
        
(Aizvietojiet 'lietotajs.txt' ar pareizo faila ceļu),
faila_ceels = 'lietotajs.txt'
lasit_un_drukat(faila_ceels)

def lasit_un_drukats(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_key:
            saturs = faila_key.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")


faila_ceels = 'lietotajs.txt'
lasit_un_drukat(faila_ceels)

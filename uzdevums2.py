import csv

def izdrukat_otro_kolonnu(file_path, delimiter=','):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_atslega:
            lasitajs = csv.reader(faila_atslega, delimiter=delimiter)
            
            for rinda in lasitajs:
                if len(rinda) >= 2:
                    print(rinda[1])
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

def izdrukat_treso_rindu(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_key:
            rindu_saraksts = faila_key.readlines()
            
            if len(rindu_saraksts) >= 3:
                print("Trešās rindas saturs:")
                print(rindu_saraksts[2])  
            else:
                print("Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

faila_ceels_csv = 'jusu_faila_ceels.csv'
izdrukat_otro_kolonnu(faila_ceels_csv)

faila_ceels_txt = 'jusu_faila_ceels.txt'
izdrukat_treso_rindu(faila_ceels_txt)


def izdrukaju_treso_rindu(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as faila_atslega:
            rindu_saraksts = faila_atslega.readlines()
            
        
            if len(rindu_saraksts) >= 3:
                print("Trešās rindas saturs:")
                print(rindu_saraksts[2])  
            else:
                print("Failā nav pietiekam daudz rindu.")
    except FileNotFoundError:
        print(f"Faila '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")


faila_ceels = 'jusu_faila_ceels.txt'
izdrukaju_treso_rindu(faila_ceels)
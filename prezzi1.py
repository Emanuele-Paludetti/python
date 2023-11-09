def prezzo_medio(tupla,prodotto,giorno):
    for nomi,giorni,prezzi in tupla:


prezzi_prodotti=(
                ("Mela","Lunedì",1.2),
                ("Mela","Lunedì",1.1),
                ("Pera","Lunedì",1.3),
                ("Pera","Martedì",1.5),
                ("Banana","Mercoledì",1.2),
                ("Pera","Martedì",1.6),
                ("Banana","Giovedì",0.7),
                )

prodotto=str(input("Inserisci il prodotto di cui vuoi sapere il prezzo medio: "))
giorno=str(input("Inserisci il giorno interessato: "))
assenza= True
while True:
    for nomi, giorni, prezzi in prezzi_prodotti:
        if (nomi!=prodotto):
            assenza=False
        else:
            assenza=True
            break

    if(assenza==False):
        print("Il prodotto non esiste")
        prodotto=str(input("Inserisci il prodotto di cui vuoi sapere il prezzo medio: "))

prezzo_medio(prezzi_prodotti,prodotto,giorno)

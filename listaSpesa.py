lista_spesa =[]

def aggiungiElementi():
    elemento = input("Inserisci l'elemento da aggiungere:")
    lista_spesa.append(elemento)
    print("lelemento aggiunto alla lista e':" + elemento)

def visuaElementi():
 for i in range (len(lista_spesa)):
    print(f"{i + 1 }. {lista_spesa[i]}")
  
def rimuoviElementi():
    elemento= int(input())
    lista_spesa.pop(elemento)


def contaElementi():
   print(f"Numero di elementi nella lista : {len(lista_spesa)}")

def svuotaLista():
   lista_spesa.clear()

while True:
   print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
   x=int(input(""))
   if x == 0:
        break
   elif x == 1:
        aggiungiElementi()
   elif x == 2:
          visuaElementi()
   elif x == 3:
          rimuoviElementi()
   elif x == 4:
           contaElementi()
   elif x == 5:
        svuotaLista()
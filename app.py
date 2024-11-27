from flask import Flask, request

app = Flask(__name__)

# Variabile globale per la lista della spesa
lista_spesa = []

# Rotta principale per visualizzare la lista della spesa
@app.route('/')
def home():
    return str(lista_spesa) if lista_spesa else "La lista della spesa è vuota."

# Rotta per aggiungere un elemento alla lista della spesa
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    item = request.form.get('item')
    if item:
        lista_spesa.append(item)
        return f"Elemento '{item}' aggiunto alla lista.", 200
    return "Nessun elemento fornito.", 400

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)

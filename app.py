from flask import Flask, render_template, request, redirect, url_for
#inizializza l'app Flask
app = Flask(__name__)
#rotta principale
lista_spesa=[]
@app.route('/')
def home():
    return render_template('index.html',lista=lista_spesa)


@app.route('/aggiungi', methods=['POST'])
def aggiungi():
#ottiene elemento dal form
    elemento = request.form['elemento']
#aggiunge alla lista
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota_lista():
    lista_spesa.clear()
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
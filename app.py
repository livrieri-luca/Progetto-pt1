from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'  # URI del database SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disabilita il tracking delle modifiche
db = SQLAlchemy(app)  # Inizializza SQLAlchemy con l'app Flask

# Modello della tabella ListaSpesa
class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID unico per ogni elemento
    elemento = db.Column(db.String(100), nullable=False, unique=True)  # Nome dell'elemento (stringa non nulla, unico)

    def __repr__(self):
        return f'<ListaSpesa {self.elemento}>'

# Crea le tabelle nel database (se non esistono già)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()  # Recupera tutti gli elementi dalla tabella
    return render_template('home.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']  # Ottieni l'elemento dal form
    if elemento:
        # Verifica se l'elemento esiste già nella lista
        if ListaSpesa.query.filter_by(elemento=elemento).first():
            return render_template('home.html', lista=ListaSpesa.query.all(), error="Elemento già presente nella lista.")
        
        nuovo_elemento = ListaSpesa(elemento=elemento)  # Crea un nuovo oggetto ListaSpesa
        db.session.add(nuovo_elemento)  # Aggiungi l'elemento alla sessione del database
        db.session.commit()  # Commit per salvare le modifiche
    return redirect(url_for('home'))  # Ritorna alla home page

@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    elemento = ListaSpesa.query.get_or_404(id)  # Recupera l'elemento da eliminare
    db.session.delete(elemento)  # Elimina l'elemento dalla sessione
    db.session.commit()  # Commit per applicare la modifica
    return redirect(url_for('home'))  # Ritorna alla home page

@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete()  # Elimina tutti gli elementi dalla tabella
    db.session.commit()  # Commit per applicare la modifica
    return redirect(url_for('home'))  # Ritorna alla home page

if __name__ == '__main__':
    app.run(debug=True)

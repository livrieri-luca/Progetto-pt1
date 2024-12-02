from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Inizializzazione dell'oggetto SQLAlchemy

class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID unico per ogni elemento
    elemento = db.Column(db.String(100), nullable=False)  # Nome dell'elemento (stringa non nulla)

    def __repr__(self):
        return f'<ListaSpesa {self.elemento}>'

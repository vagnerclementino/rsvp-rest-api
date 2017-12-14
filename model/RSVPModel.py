from rsvp import db


class RSVPModel(db.Model):
    __tablename__ = 'confirmacao_presenca'
    __table_args__ = {"schema":"rsvp"}

    id_confirmacao_presenca = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String())
    evento= db.Column(db.String())
    acompanhante = db.Column(db.String())
    observacao = db.Column(db.String())

    def __init__(self, nome, email, evento, acompanhante, observacao):
        self.nome = nome
        self.email = email
        self.evento = evento
        self.acompanhante = acompanhante
        self.observacao = observacao

    def __repr__(self):
        return '<nome: {}>'.format(self.nome)

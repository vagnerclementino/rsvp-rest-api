import app


class RSVPModel(app.db.Model):
    __tablename__ = 'confirmacao_presenca'
    __table_args__ = {"schema": "rsvp"}

    id_confirmacao_presenca = app.db.Column(app.db.Integer, primary_key=True)
    nome = app.db.Column(app.db.String())
    email = app.db.Column(app.db.String())
    evento = app.db.Column(app.db.String())
    acompanhante = app.db.Column(app.db.String())
    observacao = app.db.Column(app.db.String())

    def __init__(self, nome, email, evento, acompanhante, observacao):
        self.nome = nome
        self.email = email
        self.evento = evento
        self.acompanhante = acompanhante
        self.observacao = observacao

    def __repr__(self):
        return '<nome: {}>'.format(self.nome)

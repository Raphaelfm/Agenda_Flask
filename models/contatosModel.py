from database.data import conectar;

class Contato:
    def __init__(self,id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    @staticmethod
    def obter_todos():
        db = conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contatos")
        resultados = cursor.fetchall()
        contatos = []
        for resultado in resultados:
            contatos.append(Contato(resultado[0], resultado[1], resultado[2], resultado[3]))
        cursor.close()
        db.close()
        return contatos

    def salvar(self):
        db = conectar()
        cursor = db.cursor()
        sql = "INSERT INTO contatos (nome, email, telefone) VALUES (%s, %s, %s)"
        valores = (self.nome, self.email, self.telefone)
        cursor.execute(sql, valores)
        db.commit()
        cursor.close()
        db.close()

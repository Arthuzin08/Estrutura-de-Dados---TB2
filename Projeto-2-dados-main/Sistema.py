class Cliente:
    def __init__(self, id_cliente, nome, telefone, prioridade):
        self.id = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "prioridade": self.prioridade
        }
    
class Atendente:
    def __init__(self, id_atendente, nome):
        self.id = id_atendente
        self.nome = nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

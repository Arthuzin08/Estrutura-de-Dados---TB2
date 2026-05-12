from datetime import datetime

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

class Atendimento:
    def __init__(self, cliente, atendente):
        self.cliente = cliente
        self.atendente = atendente
        self.inicio = datetime.now()
        self.fim = None
        self.duracao = None

    def finalizar(self):
        self.fim = datetime.now()
        self.duracao = (self.fim - self.inicio).seconds

    def to_dict(self):
        return {
            "cliente": self.cliente.nome,
            "atendente": self.atendente.nome,
            "inicio": str(self.inicio),
            "fim": str(self.fim),
            "duracao": self.duracao
        }

class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, cliente):
        novo = No(cliente)

        if self.inicio is None:
            self.inicio = novo
            return

        atual = self.inicio

        while atual.proximo:
            atual = atual.proximo

        atual.proximo =      novo   

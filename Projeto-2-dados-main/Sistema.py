import json
from collections import deque
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

    def remover(self, id_cliente):
        atual = self.inicio
        anterior = None

        while atual:

            if atual.cliente.id == id_cliente:

                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                return True

            anterior = atual
            atual = atual.proximo

        return False

    def listar(self):
        atual = self.inicio

        while atual:
            print(
                f"ID: {atual.cliente.id} | "
                f"Nome: {atual.cliente.nome}"
            )

            atual = atual.proximo


fila_prioridade = deque()
fila_comum = deque()

pilha_desfazer = []

clientes = []
atendentes = []
historico = []

clientes_ativos = ListaEncadeada()

atendimento_atual = None

def registrar_log(mensagem):

    with open("logs.txt", "a", encoding="utf-8") as arquivo:

        arquivo.write(
            f"{datetime.now()} - {mensagem}\n"
        )


def salvar_dados():

    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            [c.to_dict() for c in clientes],
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    with open("atendentes.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            [a.to_dict() for a in atendentes],
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    with open("historico.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            [h.to_dict() for h in historico],
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def busca_binaria(id_cliente):

    inicio = 0
    fim = len(clientes) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if clientes[meio].id == id_cliente:
            return clientes[meio]

        elif clientes[meio].id < id_cliente:
            inicio = meio + 1

        else:
            fim = meio - 1

    return None


def imprimir_historico_recursivo(lista, indice=0):

    if indice >= len(lista):
        return

    atendimento = lista[indice]

    print(
        f"Cliente: {atendimento.cliente.nome} | "
        f"Atendente: {atendimento.atendente.nome} | "
        f"Duração: {atendimento.duracao}s"
    )

    imprimir_historico_recursivo(
        lista,
        indice + 1
    )


def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):

    resultado = []

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):

        if esquerda[i].duracao <= direita[j].duracao:
            resultado.append(esquerda[i])
            i += 1

        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

def cadastrar_cliente():

    try:

        id_cliente = int(input("ID do cliente: "))

        if busca_binaria(id_cliente):
            print("Cliente já existe")
            return

        nome = input("Nome: ")
        telefone = input("Telefone: ")

        prioridade = input(
            "Cliente prioritário? (s/n): "
        ).lower() == "s"

        cliente = Cliente(
            id_cliente,
            nome,
            telefone,
            prioridade
        )

        clientes.append(cliente)

        clientes.sort(key=lambda c: c.id)

        clientes_ativos.adicionar(cliente)

        salvar_dados()

        registrar_log(
            f"Cliente cadastrado: {nome}"
        )

        print("Cliente cadastrado com sucesso")

    except:
        print("Erro ao cadastrar cliente")


def cadastrar_atendente():

    try:

        id_atendente = int(
            input("ID do atendente: ")
        )

        nome = input("Nome: ")

        atendente = Atendente(
            id_atendente,
            nome
        )

        atendentes.append(atendente)

        salvar_dados()

        registrar_log(
            f"Atendente cadastrado: {nome}"
        )

        print("Atendente cadastrado")

    except:
        print("Erro ao cadastrar atendente")
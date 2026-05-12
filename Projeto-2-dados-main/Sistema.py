import csv
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

def abrir_atendimento():

    try:

        id_cliente = int(
            input("ID do cliente: ")
        )

        cliente = busca_binaria(id_cliente)

        if not cliente:
            print("Cliente não encontrado")
            return

        if cliente.prioridade:
            fila_prioridade.append(cliente)
        else:
            fila_comum.append(cliente)

        registrar_log(
            f"Cliente entrou na fila: {cliente.nome}"
        )

        print("Cliente adicionado na fila")

    except:
        print("Erro ao abrir atendimento")



def chamar_proximo():

    global atendimento_atual

    if atendimento_atual:
        print("Já existe atendimento em andamento")
        return

    if len(atendentes) == 0:
        print("Nenhum atendente cadastrado")
        return

    if fila_prioridade:

        cliente = fila_prioridade.popleft()

    elif fila_comum:

        cliente = fila_comum.popleft()

    else:
        print("Fila vazia")
        return

    atendente = atendentes[0]

    atendimento_atual = Atendimento(
        cliente,
        atendente
    )

    registrar_log(
        f"Início atendimento: {cliente.nome}"
    )

    print(
        f"Atendendo cliente: {cliente.nome}"
    )


def finalizar_atendimento():

    global atendimento_atual

    if not atendimento_atual:
        print("Nenhum atendimento em andamento")
        return

    atendimento_atual.finalizar()

    historico.append(atendimento_atual)

    pilha_desfazer.append(atendimento_atual)

    registrar_log(
        f"Atendimento finalizado: "
        f"{atendimento_atual.cliente.nome}"
    )

    salvar_dados()

    print("Atendimento finalizado")

    atendimento_atual = None


def desfazer_ultima_finalizacao():

    if not pilha_desfazer:
        print("Nada para desfazer")
        return

    ultimo = pilha_desfazer.pop()

    historico.remove(ultimo)

    registrar_log(
        f"Desfeito atendimento: "
        f"{ultimo.cliente.nome}"
    )

    print("Última finalização desfeita")



def historico_cliente():

    id_cliente = int(
        input("ID do cliente: ")
    )

    cliente = busca_binaria(id_cliente)

    if not cliente:
        print("Cliente não encontrado")
        return

    encontrados = []

    for atendimento in historico:

        if atendimento.cliente.id == cliente.id:
            encontrados.append(atendimento)

    if not encontrados:
        print("Nenhum histórico")
        return

    imprimir_historico_recursivo(encontrados)

def remover_cliente():

    id_cliente = int(
        input("ID do cliente: ")
    )

    if atendimento_atual:

        if atendimento_atual.cliente.id == id_cliente:
            print(
                "Cliente possui atendimento aberto"
            )
            return

    removido = clientes_ativos.remover(
        id_cliente
    )

    if removido:
        print("Cliente removido")
    else:
        print("Cliente não encontrado")


def relatorio_tempo_medio():

    if len(historico) == 0:
        print("Sem histórico")
        return

    soma = 0

    for atendimento in historico:
        soma += atendimento.duracao

    media = soma / len(historico)

    print(
        f"Tempo médio: {media:.2f} segundos"
    )


def top_5_clientes():

    contador = {}

    for atendimento in historico:

        nome = atendimento.cliente.nome

        contador[nome] = (
            contador.get(nome, 0) + 1
        )

    ranking = sorted(
        contador.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTOP 5 CLIENTES")

    for cliente, qtd in ranking[:5]:

        print(
            f"{cliente} - {qtd} atendimentos"
        )

def exportar_csv():

    with open(
        "relatorio.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            "Cliente",
            "Atendente",
            "Duração"
        ])

        for atendimento in historico:

            writer.writerow([
                atendimento.cliente.nome,
                atendimento.atendente.nome,
                atendimento.duracao
            ])

    print("CSV exportado")



def alerta_espera():

    total = (
        len(fila_prioridade) +
        len(fila_comum)
    )

    if total >= 5:

        print(
            "ALERTA: fila com tempo de espera alto"
        )

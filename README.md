# Estrutura-de-Dados---TB2

# Projeto 2 - Sistema Completo de Atendimento e Análise

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de Estrutura de Dados e tem como objetivo criar um sistema completo de gerenciamento de atendimentos para uma clínica ou central de atendimento.

O sistema permite cadastrar clientes e atendentes, organizar filas de atendimento comum e prioritário, registrar histórico de atendimentos, gerar relatórios e realizar buscas rápidas utilizando busca binária.

Além disso, o projeto aplica conteúdos estudados durante a disciplina, como vetores, filas, pilhas, listas encadeadas, ordenação, recursão e análise de complexidade Big-O.

---

# 🎯 Objetivo

Desenvolver um sistema de atendimento capaz de:

- Cadastrar clientes e atendentes;
- Organizar filas de atendimento;
- Registrar histórico;
- Gerar relatórios;
- Utilizar estruturas de dados na prática;
- Aplicar algoritmos de busca e ordenação.

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- JSON
- CSV
- Git/GitHub

---

# 📂 Organização do Projeto

```bash
Estrutura-de-Dados---TB2-main/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── clientes.json
│   ├── atendentes.json
│   └── historico.json
│
├── src/
│   ├── clientes.py
│   ├── atendentes.py
│   ├── atendimento.py
│   ├── filas.py
│   ├── relatorios.py
│   └── persistencia.py
│
└── tests/
    └── test_basico.py
```

---

# ⚙️ Funcionalidades

## Cadastro de Clientes

O sistema permite cadastrar clientes contendo:

- ID
- Nome
- Telefone
- Prioridade

---

## Cadastro de Atendentes

Permite cadastrar atendentes com:

- ID
- Nome

---

## Filas de Atendimento

O sistema possui:

- Fila comum
- Fila prioritária

Clientes prioritários possuem preferência no atendimento, mantendo a ordem de chegada.

---

## Chamada de Atendimento

O sistema chama primeiro os clientes da fila prioritária. Caso ela esteja vazia, chama o próximo cliente da fila comum.

---

## Finalização de Atendimento

Ao finalizar um atendimento, o sistema registra:

- Cliente
- Atendente
- Data
- Duração do atendimento

---

## Histórico de Atendimentos

O sistema permite consultar o histórico de atendimentos de um cliente.

---

## Desfazer Última Finalização

Uma pilha é utilizada para desfazer a última finalização de atendimento.

---

## Busca Binária

A busca de clientes é feita utilizando vetor ordenado por ID e busca binária.

Complexidade:

```bash
O(log n)
```

---

## Exportação CSV

Os relatórios podem ser exportados em formato CSV.

---

# 🧱 Estruturas de Dados Utilizadas

| Estrutura | Aplicação |
|---|---|
| Vetor ordenado | Busca binária |
| Fila comum | Atendimento normal |
| Fila prioritária | Atendimento urgente |
| Pilha | Desfazer ação |
| Lista encadeada | Controle de clientes |
| Ordenação | Relatórios |

---

# 📜 Regras de Negócio

- Clientes prioritários têm preferência;
- A ordem de chegada deve ser mantida;
- Não é permitido finalizar atendimento sem cliente;
- Não é permitido remover cliente com atendimento em aberto;
- IDs não podem ser duplicados.

---

# 💾 Persistência de Dados

Os dados são armazenados em arquivos JSON para manter as informações salvas.

Arquivos utilizados:

```bash
clientes.json
atendentes.json
historico.json
```

---

# ▶️ Como Executar

## 1. Clone o repositório

```bash
git clone <link-do-repositorio>
```

## 2. Acesse a pasta do projeto

```bash
cd Estrutura-de-Dados---TB2-main
```

## 3. Execute o sistema

```bash
python main.py
```

---

# 🧪 Testes

O projeto possui testes básicos para validar funcionalidades importantes do sistema.

---

# 🔄 Versionamento

O projeto utiliza Git e GitHub para controle de versão.

Exemplos de commits:

```bash
git commit -m "Cria cadastro de clientes"
git commit -m "Implementa fila de prioridade"
git commit -m "Adiciona busca binaria"
```

---

# 👨‍💻 Autor

Projeto desenvolvido para a disciplina de Estrutura de Dados.

Alunos: Arthur Lima;
        Bruno Juvenal;
        Fredson Vicente;
        Gustavo Dias;
        Igor Medeiros;
        Lucas Libanio.


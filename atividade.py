"""
🧠 Atvidade Prática - Sistema de cadastro de produto | Dia 03/03
 
🎯 Objetivo da Atividade
Praticar o uso de dicionários em Python, armazenando e manipulando informações de um produto.
 
 
📋 Cenário
Uma pequena loja de tecnologia chamada Devoc Technology está começando a organizar seu estoque utilizando um sistema simples em Python.
 
Cada produto da loja precisa ter algumas informações armazenadas em um dicionário.
 
 
🔧 O que você deve fazer
Criar um dicionário chamado produto contendo as seguintes informações:
nome do produto
preço
quantidade em estoque
categoria
Depois disso o programa deve:
Mostrar todas as informações do produto
Mostrar apenas o nome do produto
Mostrar apenas o preço do produto
Atualizar a quantidade em estoque
 
 
💻 Exemplo de dicionário
produto = {
    "nome": "Mouse Gamer",
    "preco": 150,
    "estoque": 20,
    "categoria": "Periféricos"
}
 
💻 Exemplo de saída esperada
Produto cadastrado:
{'nome': 'Mouse Gamer', 'preco': 150, 'estoque': 20, 'categoria': 'Periféricos'}
Nome do produto: Mouse Gamer
Preço do produto: 150
 
✅ Critérios para a atividade estar correta
Criar um dicionário
Utilizar pelo menos 4 chaves
Acessar valores do dicionário
 
⭐ Desafio extra (opcional)
 
Criar uma lista de produtos, onde cada produto é um dicionário e incrementar a lista.
 
Exemplo:
produtos = [
    {"nome": "Mouse", "preco": 150},
    {"nome": "Teclado", "preco": 200},
    {"nome": "Monitor", "preco": 1200}
]
 
Mostrar todos os produtos utilizando um for.
 
📁 Nome do arquivo
exercicio_dicionario.py
"""


produto1 = input("qual o produto? ")
preco = input("qual o valor? ")
estoque = input("quantos no estoque? ")
categoria = input("qual categoria pertence? ")

Produtos = {
    "produto1": produto1, "preco": preco, "estoque": estoque, 'categoria': categoria
    }



print(Produtos["produto1"])
print(Produtos["preco"])
print(Produtos["estoque"])
print(Produtos["categoria"])



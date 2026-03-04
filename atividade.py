lista_produtos = []

while True:

    produto1 = input("qual o produto? ")
    preco = float(input("qual o valor? "))
    estoque = int(input("quantos no estoque? "))
    categoria = input("qual categoria pertence? ")

    Produtos = {
        "produto1": produto1, "preco": preco, "estoque": estoque, 'categoria': categoria
        }
    
    lista_produtos.append(Produtos)

    print(Produtos["produto1"])
    print(Produtos["preco"])
    print(Produtos["estoque"])
    print(Produtos["categoria"])

    pergunta = input("Você deseja adicionar mais produtos? Digite S ou N. ").upper()

    if pergunta != "S":
        print("Encerrando cadastro...")
        print(lista_produtos)

        break



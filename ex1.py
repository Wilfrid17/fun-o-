def cadastra_produto(): #cria função para cadastra produto
    produto = input("Digite o nome do produto: ") #pede para digitar o nome do produto
    produto = produto.casefold() #transforma o produto em maiusculo
    produto = produto.strip() #remove os espaços em branco
    print(f"Produto {produto} foi cadastrado com sucesso")

for i in range(3): #para i no intervalo de 3
    cadastra_produto() #chama a função cadastra produto

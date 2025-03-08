
def cadastra_produto(): #cria uma função para cadastrar produto
    produto = input("Digite o nome do produto: ")
    produto = produto.casefold() #transforma o produto em minusculo
    produto = produto.strip() #remove os espaços em branco
    return produto #retorna o produto
    
for i in range(3): #para i no intervalo de 3
    produto = cadastra_produto() #chama a função cadastra produto e armazena o produto
    print(produto)

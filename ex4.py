
#Vamos criar uma function com parâmetro
#Digamos que estamos criando um programa para categorizar os produtos de uma revendedora de bebidas.
#Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.

def eh_da_categoria(bebida, cod_categoria): #bebida é o produto e cod_categoria é a categoria do produto
    bebida = bebida.upper() #transforma a bebida em maiúsculo
    if cod_categoria in bebida: #verificar se a categoria está na bebida
        return True #retorna verdadeiro
    else:
        return False #retorna falso
    
produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

#Crie um programa que analise uma lista de produtos e envie instruções para a equipe de estoque dizendo quais produtos devem ser enviados para a área de bebidas alcóolicas.

for produto in produtos: #para cada produto na lista de produtos
    produto = produto.upper() #transforma o produto em maiúsculo
    if eh_da_categoria(produto, 'BEB'): #verificar se o produto é da categoria BEB
        print(f"Enviar {produto} para setor de bebidas alcolicas:")
    elif eh_da_categoria(produto, 'BSA'): #verificar de o produto é da categoria BSA
        print(f"Enviar {produto} para setor de bebidas não alcolicas")
        

qtde_produtos = len(produtos) #conta a quantidade de produtos
print(f"Quantidade de produto são: {qtde_produtos}")
debito = 0
#função que calcula e retorna o preço final, de acordo com o desconto aplicado sobre o preço.
def calcular_preco_final(preco, desconto):
    preco_final = preco - (preco * desconto/100)
    return preco_final

#função para organizar a saída.
def mostrarLinhas():
    print('=-'*20)


#laço de repetição para obter 3 produtos diferentes.
for x in range (3):

    preco_original = float(input("Digite o preço do produto: "))
    preco_desconto = int(input("Digite o percentual de desconto: "))
    mostrarLinhas()
    print(f'Produto: {x+1}')

    #armazenando a função calcular_preco_final em uma variável para calcular o total com os descontos.
    preco_final = calcular_preco_final(preco_original, preco_desconto)
    print(f'Preço original R$ {preco_original} | Desconto: {preco_desconto}% | Preço final R$ {preco_final}')
    mostrarLinhas()
    debito += preco_final

print(f'Total a pagar: R$ {debito}')

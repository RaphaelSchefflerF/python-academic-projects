cont=0
custom=0
calVenda=0
mediacusto=0
while cont<5:
    custo=int(input('Digite o preço de Custo:'))
    vend=int(input('Digite o preço de Venda:'))
    qtVend=int(input('Digite a QT vendida em 1 mes:'))
    calLucro=(vend-custo)*qtVend
    if custo>10:
        custom=custom + 1
    calVenda= calVenda+(vend * qtVend)
    mediacusto= mediacusto + custo
    cont= cont+1
print('Qt de Produtos Acima de R$ 10,0:',custom)
print('Valor Arrecadado com a Venda de todos os produtos:',calVenda)
print('Medias dos Custos:',mediacusto/5)


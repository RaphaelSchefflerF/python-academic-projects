cont=0
contLucro=0
contMedia=0
while cont<5:
    prCompra=int(input('Preço de Compra:'))
    prVenda=int(input('Preço de Venda:'))
    
    soma=prVenda-prCompra
    
    print('Lucro da Escultura:',soma)
    
    contMedia=contMedia+soma
    cont= cont+1
    print('===========================')
    
print('Média dos Lucros:',contMedia/5)
    
    

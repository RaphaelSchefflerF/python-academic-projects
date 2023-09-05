
class Les:
    def __init__(self,tam_maximo):
        self.tam_maximo= tam_maximo
        self.vetor=[None]*tam_maximo
        self.quant=0

    def inserir_fim(self,valor):
        self.vetor[self.quant]=valor
        self.quant+=1
        
    def esta_cheia(self):
        return self.quant == self.tam_maximo

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i])
            
    def remover_fim(self):
        self.quant-=1

    
        
        
    


'''    
        if self.quant == self.tam_maximo:
            return True
        return False
'''
'''
    def inserir_fim(self,valor):
        if self.quant == self.tam_maximo:
            return False
            #print('Tá Cheio')
        else:
            self.vetor[self.quant]=valor
            self.quant+=1
            return True
'''        

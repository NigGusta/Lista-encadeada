class No:
    def __init__(self, valor):
        self.valor = valor  
        self.proximo = None  

class ListaEncadeada:
    def __init__(self):
      self.primeiro = None  
    
    def vazia(self):
        if len(self.lista) == 0:
          print("Lista vazia!")
        else:
         print("Lista contém dados!")
    
    def tamanho(self):
        tamanho = 0 
        no_atual = self.primeiro  # começa pelo primeiro nó da lista
        while no_atual:
            tamanho += 1  
            no_atual = no_atual.proximo  # move para o próximo nó
        print("O tamanho da lista é",tamanho) 
    
    def valor(self, posicao):
        indice = 0  
        no_atual = self.primeiro  
        while no_atual and indice < posicao:
            indice += 1 
            no_atual = no_atual.proximo  
        if no_atual:
            print("o valor dessa posição : ",no_atual.valor)  
        else:
            raise IndexError('Índice fora dos limites da lista')
    
    def modificar(self, posicao, valor):
        indice = 0  
        no_atual = self.primeiro 
        while no_atual and indice < posicao:
            indice += 1  
            no_atual = no_atual.proximo  
        if no_atual:
            no_atual.valor = valor  
        else:
            print('Índice fora dos limites da lista')
    
    def inserir(self, posicao, valor):
        novo_no = No(valor)  
        if posicao == 0:  
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
          
        else:  
            indice = 0  
            no_atual = self.primeiro  
            while no_atual and indice < posicao - 1:
                indice += 1  
                no_atual = no_atual.proximo  
            if no_atual:
                novo_no.proximo = no_atual.proximo
                no_atual.proximo = novo_no
            else:
                print('Índice fora dos limites da lista')
    def remover(self, valor):
          if self.primeiro.valor == valor:
            self.primeiro = self.proximo
            return

            
lista = ListaEncadeada()

print(lista.vazia())  
lista.inserir(0, 10)
lista.inserir(1, 20)
lista.inserir(1, 15)


print(lista.vazia())  


print(lista.valor(0))  
print(lista.valor(1))  
print(lista.valor(2)) 

lista.modificar(1, 25)

(lista.valor(1)) 

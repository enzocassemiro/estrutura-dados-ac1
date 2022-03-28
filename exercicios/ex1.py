################# ESCREVA SEU CÓDIGO AQUI  ###############################
class CalcCientifica:
  
    def __init__(self,number) -> None:
        self.number = number
        
    def potencia(self, expoente = 2):
        return self.number ** expoente

    def raiz(self, indice = 2):
        return self.number ** (1/indice)

    def fatorial(self):
        num = self.number

        if self.number==1:
            return 1
        self.number -= 1

        return num * self.fatorial()


##########################################################################

# testando a classe criada
num1 = 9
num2 = 8

# cria dois objetos - um para cada numero
calc1 = CalcCientifica(num1)
calc2 = CalcCientifica(num2)

# calcula a raiz quadra 
raiz1 = calc1.raiz()
raiz2 = calc2.raiz(indice=3)

# calcula a raiz quadra 
potencia1 = calc1.potencia()
potencia2 = calc2.potencia(expoente=4)


# calcula o fatorial
fact1 = calc1.fatorial()
fact2 = calc2.fatorial()

print('Resultado esperado: ')
print('\tRaiz quadrada de 9: 3')
print('\t9 elevado a 2: 81')
print('\tFatorial de 9: 362880')

print('\n\n\tRaiz cubica de 8: 2')
print('\t8 elevado a 4: 4096')
print('\tFatorial de 8: 40320')

print('\n' + 20*'-')
print('Resultado retornado: ' )
print('\tRaiz quadrada de %d: %d' %(num1,raiz1))
print('\t%d elevado a 2: %d' %(num1,potencia1))
print('\tFatorial de %d: %d' %(num1,fact1))

print('\n\tRaiz cubica de %d: %d' %(num2,raiz2))
print('\t%d elevado a 4: %d' %(num2,potencia2))
print('\tFatorial de %d: %d' %(num2,fact2))

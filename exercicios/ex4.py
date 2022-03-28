################# ESCREVA SEU CÓDIGO AQUI  ###############################
def retornaMenor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return min(lista[0],retornaMenor(lista[1:]))
    
##########################################################################

# testando a função criada
lista = [10,6,2,9,8,23,5]
menor = retornaMenor(lista)

print('Resultado esperado: 2')

print('\n' + 20*'-')
print('Resultado retornado: %d' %(menor) )
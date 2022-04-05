################# ESCREVA SEU CÓDIGO AQUI  ###############################

def buscaBinaria(lista, numBuscado):
    first_index = -1
    last_index = -1

    for index,i in enumerate(lista):
        if i == numBuscado and first_index == -1:
            first_index = index
        if i == numBuscado and first_index!=-1:
            last_index = index

    return first_index, last_index
##########################################################################

# testando a função criada
lista = [1,2,3,4,5,5,5,5,5,6,7,8,8,8,9,10]

print('\n' + 30*'=' + '\nPrimeiro teste')
numBuscado = 5
firstIndex, lastIndex = buscaBinaria(lista, numBuscado)

print('\nResultado esperado:')
print('\tPrimeiro índice: 4')
print('\tÚltimo índice: 8')

print('\n' + 20*'-')
print('Resultado retornado:' )
print('\tPrimeiro índice: %d' %(firstIndex))
print('\tÚltimo índice: %d' %(lastIndex))

print('\n' + 30*'=' + '\nSegundo teste')
numBuscado = 50
firstIndex, lastIndex = buscaBinaria(lista, numBuscado)

print('\nResultado esperado:')
print('\tPrimeiro índice: -1')
print('\tÚltimo índice: -1')

print('\n' + 20*'-')
print('Resultado retornado:' )
print('\tPrimeiro índice: %d' %(firstIndex))
print('\tÚltimo índice: %d' %(lastIndex))
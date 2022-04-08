################# ESCREVA SEU CÓDIGO AQUI  ###############################

def buscaBinaria(lista, valorBusc, primeiroIndice=0, ultimoIndice=-1):
     
  # inicializa qual o último índice da lista
    if ultimoIndice==-1:
        ultimoIndice = len(lista)-1
  
  # obtem o indice do meio da lista
    meio = int( (primeiroIndice+ultimoIndice)/2 )
    tamanho = len(lista)

  # primeiro caso base da recursao
    if lista[meio] == valorBusc:
        j = 0
        l = 0

        for i in range(meio,0,-1):
            if lista[meio-j] == valorBusc:
                primeiroIndice = meio-j
                j+=1
            else:
                break
            
        for k in range(meio,tamanho):
            if (lista[meio+l] == valorBusc):
                ultimoIndice = meio + l
                l += 1
            else: 
                break

        return primeiroIndice, ultimoIndice
  
    elif primeiroIndice >= ultimoIndice:
        primeiroIndice = - 1
        ultimoIndice = - 1
        return primeiroIndice, ultimoIndice

    else:
      
        if valorBusc <= lista[meio]:
            ultimoIndice = meio-1
      
        else:
            primeiroIndice = meio+1

    return buscaBinaria(lista, valorBusc, primeiroIndice, ultimoIndice)
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
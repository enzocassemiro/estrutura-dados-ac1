################# ESCREVA SEU CÓDIGO AQUI  ###############################
def contaPalavras(lista):
    new_lista = []

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            new_lista.append(lista[i][j])

    maior_repeticao = 0
    maior_repeticao_pos = 0
    menor_repeticao = len(new_lista)
    menor_repeticao_pos = 0

    for index,k in enumerate(range(len(new_lista))):
        if new_lista.count(new_lista[k]) > maior_repeticao:
            maior_repeticao = new_lista.count(new_lista[k])
            maior_repeticao_pos = index
        if new_lista.count(new_lista[k]) < menor_repeticao:
            menor_repeticao = new_lista.count(new_lista[k])
            menor_repeticao_pos = index

    tamanho_lista = len(list(set(new_lista)))

    return tamanho_lista, new_lista[maior_repeticao_pos], new_lista[menor_repeticao_pos]

##########################################################################

# testando a função criada
lista = [
    ['Angola','Chade','Gana'],
    ['Chade','Angola','Gana','Togo'],
    ['Togo','Gana','Chade','Eritreia'],
    ['Chade','Togo','Angola']
]

total, maisRepetida, menosRepetida = contaPalavras(lista)

print('Resultado esperado:')
print('\tTotal: 5') 
print('\tPalavra que mais repetiu: Chade') 
print('\tPalavra que menos repetiu: Eritreia') 

print('\n' + 20*'-')
print('Resultado retornado:')
print('\tTotal: %d' %(total)) 
print('\tPalavra que mais repetiu: %s' %(maisRepetida)) 
print('\tPalavra que menos repetiu: %s' %(menosRepetida)) 
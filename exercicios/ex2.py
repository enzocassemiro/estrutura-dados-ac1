################# ESCREVA SEU CÓDIGO AQUI  ###############################
def retornaImpares(n, aux = 0, s = ''):
    aux = int(aux)
    if aux>n:
        return s
    
    else:
        if aux % 2 != 0:
            aux = str(aux)
            s += aux + ' '
            return retornaImpares(n, int(aux) + 1, s)
        else:
            return retornaImpares(n, int(aux) + 1, s)


##########################################################################

# testando a função criada
impares = retornaImpares(8)

print('Resultado esperado:')
print('\t1 3 5 7')

print('\n' + 20*'-')
print('Resultado retornado:')
print('\t',impares)

if impares != '1 3 5 7' and impares != '1 3 5 7 ':
    print('\nAtenção! Seu resultado foi diferente do que era esperado')
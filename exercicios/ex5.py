################# ESCREVA SEU CÓDIGO AQUI  ###############################
import datetime

date = datetime.date.today()
year = date.strftime("%Y")
year = int(year)


class Funcionario:
    
    def __init__(self, nome_funcionario,
                departamento, salario_bruto,
                ano_entrada,
                rg,
                dependentes) -> None:

        self.nome_funcionario = nome_funcionario
        self.departamento = departamento
        self.salario_bruto = salario_bruto
        self.ano_entrada = ano_entrada
        self.ano_saida = 0
        self.rg = rg
        self.statusEmprego = True
        self.dependentes = dependentes
    
    def calcSalarioLiquido(self):

        valor_dependente = self.dependentes * 20
        salario_bruto = self.salario_bruto + valor_dependente
        if salario_bruto <= 1000:
            calc_percentual = salario_bruto* 0.03
            calc_valor = salario_bruto - calc_percentual
        else:
            calc_percentual = salario_bruto * 0.05
            calc_valor = salario_bruto - calc_percentual
        
        return calc_valor

    def calcTempoServico(self):
        return year - self.ano_entrada

    def calcAumento(self):
        if self.calcTempoServico() < 5:
            calc_percentual = self.salario_bruto * 0.05
            calc_valor = self.salario_bruto + calc_percentual
        else:
            calc_percentual = self.salario_bruto * 0.08
            calc_valor = self.salario_bruto + calc_percentual
        
        return calc_valor - self.salario_bruto
    
    def retornaInfo(self):
        return str('\nNome Funcionário: ' + self.nome_funcionario +
                '\nDepartamento: ' + self.departamento +
                '\nSalario Bruto: ' + str(self.salario_bruto) +
                '\nAno Entrada: ' + str(self.ano_entrada) +
                '\nAno Saída: ' + str(self.ano_saida) +
                '\nRG: ' + self.rg +
                '\nStatus Emprego: ' + str(self.statusEmprego) +
                '\nDepententes: ' + str(self.dependentes))

##########################################################################

# testando a classe criada
nome = "Pedro Cardoso"
departamento = "TI"
salarioBruto = 5000
anoEntrada = 2000
rg = '192528'
dependentes = 5

func1 = Funcionario(
    nome, departamento, salarioBruto, 
    anoEntrada, rg, dependentes 
    )

salario = func1.calcSalarioLiquido()
tempo = func1.calcTempoServico()
aumento = func1.calcAumento()
info = func1.retornaInfo()
statusFunc = func1.statusEmprego

print('Resultado esperado: ')
print('\t O funcionário está empregado?: True')
print('\t Salario Liquido: 4845.00')
print('\t Tempo de serviço: 22 anos')
print('\t Aumento: 400.00')

print('\n\tString retornada pelo método imprimir(): ')

print('\n' + 20*'-')
print('Resultado retornado: ')
print('\t O funcionário está empregado?: %s' %(statusFunc))
print('\t Salario Liquido: %1.2f' %(salario))
print('\t Tempo de serviço: %d anos' %(tempo))
print('\t Aumento: %1.2f' %(aumento))

print('\nInformacoes da classe retornadas pela método retornaInfo: \n%s' %(info))

if not isinstance(info, str):
    print('\nAtenção. O valor retornado pelo método retornaInfo()')
    print('da classe Funcionário deveria ser uma string')
salario = float(input())

if (salario >= 0 and salario <= 400 ):
    reajuste = salario * 15 / 100
    novo_salario = salario + reajuste
    print('Novo salario: %.2f'%novo_salario)
    print('Reajuste ganho: %.2f'%reajuste)
    print('Em percentual: 15 %')
elif (salario >= 400.01 and salario <= 800.00 ):
    reajuste = salario * 12 / 100
    novo_salario = salario + reajuste
    print('Novo salario: %.2f'%novo_salario)
    print('Reajuste ganho: %.2f'%reajuste)
    print('Em percentual: 12 %')
elif (salario >= 800.01 and salario <= 1200.00 ):
    reajuste = salario * 10 / 100
    novo_salario = salario + reajuste
    print('Novo salario: %.2f'%novo_salario)
    print('Reajuste ganho: %.2f'%reajuste)
    print('Em percentual: 10 %')
elif (salario >= 1200.01 and salario <= 2000.00 ):
    reajuste = salario * 7 / 100
    novo_salario = salario + reajuste
    print('Novo salario: %.2f'%novo_salario)
    print('Reajuste ganho: %.2f'%reajuste)
    print('Em percentual: 7 %')
elif (salario > 2000.00 ):
    reajuste = salario * 4 / 100
    novo_salario = salario + reajuste
    print('Novo salario: %.2f'%novo_salario)
    print('Reajuste ganho: %.2f'%reajuste)
    print('Em percentual: 4 %')
# notas01 = float(input())
# print("NOTAS:")

# notas100 = notas01 // 100
# notas01 = notas01 % 100

# notas50 = notas01 // 50
# notas01 = notas01 % 50

# notas20 = notas01 // 20
# notas01 = notas01 % 20

# notas10 = notas01 // 10
# notas01 = notas01 % 10

# notas5 = notas01 // 5
# notas01 = notas01 % 5

# notas2 = notas01 // 2


# print("%d nota(s) de R$ 100.00" % notas100)
# print("%d nota(s) de R$ 50.00" % notas50)
# print("%d nota(s) de R$ 20.00" % notas20)
# print("%d nota(s) de R$ 10.00" % notas10)
# print("%d nota(s) de R$ 5.00" % notas5)
# print("%d nota(s) de R$ 2.00" % notas2)


# # ----------------------------------//----------------------------------

# moedas = notas01 % 2
# moedas = moedas * 100

# moeda1 = moedas // 100
# moedas = moedas % 100

# moeda50 = moedas // 50
# moedas = moedas % 50

# moeda25 = moedas // 25
# moedas = moedas % 25

# moeda10 = moedas // 10
# moedas = moedas % 10

# moeda05 = moedas // 5
# moeda01 = moedas % 5

# moeda01 = moedas // 1
# moedas = moedas % 1
# print("MOEDAS:")

# print("%d moeda(s) de R$ 1.00" % moeda1)
# print("%d moeda(s) de R$ 0.50" % moeda50)
# print("%d moeda(s) de R$ 0.25" % moeda25)
# print("%d moeda(s) de R$ 0.10" % moeda10)
# print("%d moeda(s) de R$ 0.05" % moeda05)
# print("%d moeda(s) de R$ 0.01" % moeda01)


# ----------------------------------------------------//---------------------


# reais, centavos = map(int, input().split('.'))
# centavos = centavos + reais * 100

# print('NOTAS:')
# print(f'{centavos//10000} nota(s) de R$ 100.00')
# centavos = centavos%10000
# print(f'{centavos//5000} nota(s) de R$ 50.00')
# centavos = centavos%5000
# print(f'{centavos//2000} nota(s) de R$ 20.00')
# centavos = centavos%2000
# print(f'{centavos//1000} nota(s) de R$ 10.00')
# centavos = centavos%1000
# print(f'{centavos//500} nota(s) de R$ 5.00')
# centavos = centavos%500
# print(f'{centavos//200} nota(s) de R$ 2.00')
# centavos = centavos%200

# print('MOEDAS:')
# print(f'{centavos//100} moeda(s) de R$ 1.00')
# centavos = centavos%100
# print(f'{centavos//50} moeda(s) de R$ 0.50')
# centavos = centavos%50
# print(f'{centavos//25} moeda(s) de R$ 0.25')
# centavos = centavos%25
# print(f'{centavos//10} moeda(s) de R$ 0.10')
# centavos = centavos%10
# print(f'{centavos//5} moeda(s) de R$ 0.05')
# centavos = centavos%5
# print(f'{centavos//1} moeda(s) de R$ 0.01')


# ------------------------------//---------------------------------------


reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for nota in notas:
    qtde = centavos//(nota*100)
    print('{} nota(s) de R$ {}.00'.format(qtde, nota))
    centavos = centavos%(nota*100)

moedas = [100, 50, 25, 10, 5, 1]

print("MOEDAS:")
for moeda in moedas:
    qtde = centavos//moeda
    m = moeda//100
    md = moeda%100
    print('{} moeda(s) de R$ {}.{:02}'.format(qtde, m, md))
    centavos = centavos%moeda
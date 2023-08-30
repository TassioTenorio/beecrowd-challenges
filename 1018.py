notas001 = int(input())
print(notas001)

# 100
notas100 = notas001 // 100
notas001 = notas001 % 100

notas50 = notas001 // 50
notas001 = notas001 % 50

notas20 = notas001 // 20
notas001 = notas001 % 20

notas10 = notas001 // 10
notas001 = notas001 % 10

notas5 = notas001 // 5
notas001 = notas001 % 5

notas2 = notas001 // 2
notas001 = notas001 % 2

notas1 = notas001 // 1
notas001 = notas001 % 1

# notas001 = notas001 % 100
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")


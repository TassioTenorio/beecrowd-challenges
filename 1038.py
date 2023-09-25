
codigo, quantidade = map(int, input().split())
valor = 0

if codigo == 1:
    valor = 4.0
elif codigo == 2:
    valor = 4.5
elif codigo == 3:
    valor = 5.0
elif codigo == 4:
    valor = 2.0
elif codigo == 5:
    valor = 1.5

preco = valor * quantidade
print("Total: R$ %.2f" % preco)



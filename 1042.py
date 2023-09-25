entrada = input().split()

valores = [int(i) for i in entrada]

valores.sort()

print(*valores, sep='\n')
print()
print(*entrada, sep='\n')

# # --------------------------------------------//--------------------------------------------------

# valores = input().split()

# valores_cresc = (int(i) for i in valores)

# valores_cresc.sort()

# print(valores_cresc, sep='\n')
# print(valores, sep='\n')


idade = (int(input()))

ano = idade // 365
dias = idade % 365
mes = dias // 30
dia = dias % 30

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
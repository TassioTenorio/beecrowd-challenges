hi, mi, hf, mf = map(int, input().split())

temp = hi * 60 + mi
temp2 = hf * 60 + mf

tempj = temp2 - temp
if (tempj <= 0):
	tempj = 24 * 60 + tempj

minutos = tempj % 60
horas = tempj // 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")










a, b, c, d = map(int, input().split(" "))

cd = c + d
ab = a + b

if (b > c and d > a and cd > ab and c > 0 and d > 0 and a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores não aceitos')

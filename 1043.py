l_1, l_2, l_3 = map(float, input().split())
perimetro = l_1 + l_2 + l_3
area = ((l_1 + l_2) * l_3 / 2)


if (l_3 < l_1 + l_2 and l_2 < l_1 + l_3 and l_1 < l_2 + l_3):
    print('Perimetro = %.1f' % perimetro)
else:
    print('Area = %.1f' % area)

a, b, c = map(float, input().split())
# split é para receber na mesma linha.
area_t = (a * c) / 2
area_c = 3.14159 * c ** 2
area_tr = ((a + b) * c) / 2
area_q = b**2
area_ret = a*b

print("TRIANGULO: %.3f" % area_t)
print("CIRCULO: %.3f" % area_c)
print("TRAPEZIO: %.3f" % area_tr)
print("QUADRADO: %.3f" % area_q)
print("RETANGULO: %.3f" % area_ret)

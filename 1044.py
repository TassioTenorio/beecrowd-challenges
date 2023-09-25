# num_1, num_2 = map(int, input().split())

# if (num_1 % num_2 == 0 or num_2 % num_1 == 0):
# 	print('Sao Multiplos')
# else:
# 	print('Nao sao Multiplos')

num_1, num_2 = map(int, input().split())

mult = (num_1 % num_2 == 0 or num_2 % num_1 == 0)
n_mult = (num_1 % num_2 != 0 or num_2 % num_1 != 0)

if (mult):
    print('Sao Multiplos')
elif (n_mult):
    print('Nao sao Multiplos')

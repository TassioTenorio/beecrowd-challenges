h_initial, h_final = map(int, input().split())

time = h_final - h_initial

if (time == 0):
    time_final = 24
    print(f'O JOGO DUROU {time_final} HORA(S)')
elif (time < 0):
    time_final = time + 24
    print(f'O JOGO DUROU {time_final} HORA(S)')
elif (time > 0):
    print(f'O JOGO DUROU {time} HORA(S)')

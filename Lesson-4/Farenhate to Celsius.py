tem_c = 0
print('t°C\t\tF')
while tem_c <= 100:
    tem_f = tem_c * 9 / 5 + 32
    print(f'{tem_c}\t\t{tem_f:g}')
    tem_c += 10

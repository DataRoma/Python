

mooney = input("Введите сумму вклада: ")

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit =  [int(mooney)/100*(per_cent['ТКБ']),int(mooney)/100*(per_cent['СКБ']),int(mooney)/100*(per_cent['ВТБ']),int(mooney)/100*(per_cent['СБЕР'])]
print(list(map(round, deposit)))
maxdep = max(deposit)

print("Максимальная сумма, которую вы можете заработать - " + str(int(maxdep)))

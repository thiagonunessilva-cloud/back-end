else:
if preco < menor:
menor = preco
barato = produto
continuar T =
while continuar not in 'sn':
continuar = str(input('Quer continuar? [s/n]')).strip().lower()[0]
if continuar in 'n':
break
print('Fim do programa')
print(f'0 total da compra foi (total:.2f}')
print (f'temos {cont} produtos custando mais de R$1000.00')
print (f'O produto mais barato foi {barato) e custa R${menor:.2f}')

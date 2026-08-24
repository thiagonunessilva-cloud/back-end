elif opcao == 3:
if n1 > n2:
 print(f"0 {n1} é maior que {n2}")
elif n2 > n1:
 print(f"o {n2) é maior que (n1}")
else:
 print("Ambos os números são iguais")
elif opcao == 4:
 print('informe os números novamente')
 n1 = int(input("Qual é o primeiro número?"))
 n2= int(input("Qual é o segundo número?"))
elif opcao == 5:
 print('Finalizando...')
 else:
 print('opção inválida. Tente novamente')
sleep(2)
print('Acabou')

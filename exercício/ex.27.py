# Lê o nome completo e remove espaços extras no início e fim
nome_completo = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em uma lista de strings baseada nos espaços
nome_separado = nome_completo.split()

# O primeiro nome é o índice 0 da lista
primeiro = nome_separado[0]

# O último nome é a última posição da lista (-1)
ultimo = nome_separado[-1]

print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {primeiro}')
print(f'Seu último nome é: {ultimo}')

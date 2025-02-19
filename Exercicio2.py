import numpy as np
# Exercicio 1

# times = ['Cobh Ramblers','Wexford FC','Treaty United','Cabinteely FC','Barcelona']

# print('tres primeiros colocados: ', times[:3])
# print('dois ultimos colocados: ', times[3:])

# print('times em ordem alfabetica: ', sorted(times))

# posicao_barcelona = times.index('Barcelona') + 1
# print('A colocação do Barcelona na lista é: ', posicao_barcelona)

#------------------------------------------------------

# Exercicio 2

# dinheiro = 1500
# 
# celular1 = {
#     'nome': 'celular1',
#     'preco': 2000
# }
# 
# celular2 = {
#     'nome': 'celular2',
#     'preco': 1500
# }
# 
# celular3 = {
#     'nome': 'celular3',
#     'preco': 2200
# }
# 
# celular4 = {
#     'nome': 'celular4',
#     'preco': 1800
# }
# 
# loja1 = [celular1, celular2, celular4]
# loja2 = [celular1, celular3, celular4]
# 
# 
# print("Celulares que posso comprar:")
# for celular in loja1 + loja2:
#     if celular['preco'] <= dinheiro:
#         print(f"{celular['nome']} por {celular['preco']}")
# 
# 
# celulares_loja1 = {celular['nome'] for celular in loja1}
# celulares_loja2 = {celular['nome'] for celular in loja2}
# 
# celulares_comuns = celulares_loja1.intersection(celulares_loja2)
# 
# print("Celulares presentes nas duas lojas:", end=" ")
# print(", ".join(celulares_comuns))

#------------------------------------------------------

# Exercicio 3

# nome = input("Digite o nome do aluno: ")
# media = float(input("Digite a média do aluno: "))
# 
# aluno = {
#     'nome': nome,
#     'media': media,
#     'situacao': 'AP' if media >= 50 else 'RP'
# }
# 
# print(aluno)

#------------------------------------------------------

# Exercicio 4

# pessoas_list = []
# 
# for i in range(3):
#     pessoa = input(f"Digite o nome da pessoa {i+1}: ")
#     peso = float(input(f"Digite o peso da pessoa {i+1}: "))
#     pessoa_info = {
#         'nome': pessoa,
#         'peso': peso
#     }
#     pessoas_list.append(pessoa_info)
# 
# mais_pesada = max(pessoas_list, key=lambda x: x['peso'])
# menos_pesada = min(pessoas_list, key=lambda x: x['peso'])
# 
# print(f"A pessoa mais pesada é {mais_pesada['nome']} com {mais_pesada['peso']} kg")
# print(f"A pessoa menos pesada é {menos_pesada['nome']} com {menos_pesada['peso']} kg")

#------------------------------------------------------

# Exercicio 5


# pessoas_list = []

# while True:
#     pessoa = input("Digite o nome da pessoa: ")
#     idade = float(input("Digite a idade da pessoa: "))
#     sexo = input("Qual é o sexo? ")
#     pessoa_info = {
#         'nome': pessoa,
#         'idade': idade,
#         'sexo': sexo
#     }
#     pessoas_list.append(pessoa_info)
    
#     continuar = input("Deseja adicionar mais uma pessoa? (s/n): ")
#     if continuar.lower() != 's':
#         break

# media_idades = np.mean([p['idade'] for p in pessoas_list])
# print(f"A média das idades é: {media_idades:.2f}")

# quantidade_f = sum(1 for p in pessoas_list if p['sexo'] == 'f')
# print(f"Quantidade de pessoas com sexo 'f': {quantidade_f}")

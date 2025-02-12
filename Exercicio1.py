import math

# Exercicio 1

#nome1 = input("digite seu primeiro nome: ")
#nome2 = input("digite seu ultimo nome: ")
#nome_completo = nome1 + " "  + nome2

#nome_minusculas = nome_completo.lower()
#print("Nome em letras minúsculas: ", nome_minusculas)

#nome_maiusculas = nome_completo.upper()
#print("nome em letras maiúsculas: ", nome_maiusculas)

#numero_letras = len(nome_completo.replace(" ", ""))
#print("número de letras no nome: ", numero_letras)

#nome_inatel = nome1 + " " + "do Inatel"
#print("nome inatel: ", nome_inatel)

#------------------------------------------------------
#Exercicio 2

#numeroo = input("tabuada do numero: ")
#intervaloo = input("no intervalo: ")

#numero = int(numeroo)
#intervalo = int(intervaloo)

#for i in range(1, intervalo + 1):
#    print(f"{numero} x {i} = {numero * i}")

#------------------------------------------------------
#Exercicio 3

#sexo = input("qual é seu sexo? ")

#while sexo not in ["M", "F"]:
    #sexo = input("Nope\n")

#print("parabens")

#------------------------------------------------------
#Exercicio 4

#longe = input("quão longe? ")
#longe = int(longe)
#if longe <= 200:
#    print(f"R$ {longe * 0.50}")

#else:
#    print(f"R$ {longe * 0.45}")

#------------------------------------------------------
#Exercicio 5

# numero= input("qual é o numero? ")
# numero= int(numero)

# while numero <= 1000 or numero >= 9999:
#     numero = input("Nope\n")
#     numero= int(numero)

# unidade = numero % 10
# dezena = (numero // 10) % 10
# centena = (numero // 100) % 10
# milhar = (numero // 1000) % 10

# print(f"Unidade: {unidade}")
# print(f"Dezena: {dezena}")
# print(f"Centena: {centena}")
# print(f"Milhar: {milhar}")

#------------------------------------------------------
#Exercicio 6

#numero_decimal = input("Digite um número decimal: ")
#numero_decimal = float(numero_decimal)

 
#raiz_quadrada = math.sqrt(numero_decimal)
#print(f"Raiz quadrada: {raiz_quadrada}")

#teto = math.ceil(numero_decimal)
#print(f"Função teto: {teto}")

#chao = math.floor(numero_decimal)
#print(f"Função chão: {chao}")

#parte_inteira = int(numero_decimal)
#print(f"Parte inteira: {parte_inteira}")
#Crie um programa que: Peça ao usuário dois números. Mostre: 

#A soma, subtração, multiplicação e divisão.

#Verifique: 

#Se os números são iguais.


#Se o primeiro número é maior que o segundo.


#Se pelo menos um dos números é maior que 10.

# use apenas:
# variáveis 
# print()
# input()
# sinais aritmético + - ? * / ** % 
# sinais lógicos <  > >=  <=  != == 

print() # imprime algo ambiente de teste 


var =  10 # variáveis 


# nome = input('Digite seu nome:  ') # dinamico 
# # 


# print(nome)


# nome  = 'Julia'


# nome  =  input('Nome: ')


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))


soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

sao_iguais = n1 == n2
primeiro_maior = n1 > n2

um_maior_que_dez = (n1 > 10) + (n2 > 10) > 0


print("\n--- Resultados Matemáticos ---")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

print("\n--- Resultados Lógicos (True = Sim / False = Não) ---")
print("Os números são iguais?", sao_iguais)
print("O primeiro é maior que o segundo?", primeiro_maior)
print("Pelo menos um é maior que 10?", um_maior_que_dez)



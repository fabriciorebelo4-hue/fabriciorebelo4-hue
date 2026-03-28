# 1. Pedindo o valor do produto ao usuário
valor_original = float(input("Digite o valor do produto: R$ "))

# 2. Calculando o desconto de 10% e o valor final
desconto = valor_original * 0.10
valor_final = valor_original - desconto

# 3. Fazendo as verificações lógicas (que vão gerar True ou False)
maior_que_cem = valor_final > 100
ficou_barato = valor_final < 50

# 4. Mostrando os resultados na tela
print("\n--- Resumo do Produto ---")
# O ':.2f' formata o número para ter sempre 2 casas decimais (ex: 90.00)
print(f"Valor final com desconto: R$ {valor_final:.2f}")

print("\n--- Análise de Preço (True = Sim / False = Não) ---")
print(f"O valor final é maior que 100? {maior_que_cem}")
print(f"O produto ficou barato (menor que 50)? {ficou_barato}")
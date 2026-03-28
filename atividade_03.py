# jogo de adivinhação

import random



lista_pc = ['😂','❤️','😁']
nossa_lista = ['😂','❤️','😁']

aleatorio = random.choice(lista_pc)
escolha_personagem = input('teste escolha entre essas opções 😂   ❤️   😁: ')
resultado = aleatorio == escolha_personagem


print('Acertou? ', resultado)
print('Escolha da maquina: ', aleatorio)
print('Minha escolha: ', escolha_personagem)
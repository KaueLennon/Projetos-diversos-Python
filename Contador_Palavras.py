#DESAFIO 2
# Peça ao usuário para digitar um texto e conte:
# •	O número total de palavras.
# •	Quantas vezes cada palavra aparece (diferencie maiúsculas e minúsculas).
# Use um dicionário para armazenar as palavras e suas contagens



texto = input('Digite um texto: ')

separacao = texto.split()
dicionario = {}


for palavras in separacao:
    if palavras in dicionario:
        dicionario[palavras] += 1
    else:
        dicionario[palavras] = 1

contagem_palavras = len(separacao)

for palavra, qtd in dicionario.items():
    print(f'Palavra: {palavra}, Quantidade: {qtd}')
print(f'O total de palavras são: {contagem_palavras}')
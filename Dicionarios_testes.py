#Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
# import json
quadro = {'1': {'nome':'Isabela Soares','idade': 38,'cidade': 'Campo Grande'},
          '2': {'nome':'João Gonçalves','idade': 20,'cidade': 'São Paulo'},
          '3': {'nome':'Mario da Silva','idade': 55,'cidade': 'Porto Alegre'}
}

# print(quadro['2']['cidade'])

# print(quadro.get('2', 'chave não funcionou'))

# print(json.dumps(quadro, indent=4, ensure_ascii=False))

# print(quadro.keys())


#print(json.dumps(quadro, indent=4, ensure_ascii=False))

#Adicione um campo de profissão para essa pessoa

# quadro['2']['profissional'] = 'Engenheiro'

# print(json.dumps(quadro, indent=4, ensure_ascii=False))

# pessoa_removida = quadro.pop('2')

# print(json.dumps(quadro, indent=4, ensure_ascii=False))


#Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5
# tabela ={}

# for num in range(1,6):
#     tabela[num] = num **2

# print(tabela)

# for tabela in quadro:
#     if tabela == '1':
#         print(f'Encontrou a {quadro[tabela]['nome']}')

#Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
import json
# Frase de exemplo
frase = "o rato roeu a roupa do rei de roma e a roupa do rei de roma roeu o rato"

# Convertendo a frase para minúsculas e dividindo em palavras
palavras = frase.lower().split()

# Dicionário para armazenar a frequência das palavras
frequencia = {}

# Contando a frequência de cada palavra
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1  # Incrementa a contagem se a palavra já existe
    else:
        frequencia[palavra] = 1   # Adiciona a palavra ao dicionário com contagem 1

# Exibindo o resultado
print("Frequência das palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
from datetime import datetime

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['Kaue', 'João', 'Matheus', 'Priscila']

ano_atual = datetime.now().year
lista_ano_nascimento = [1993, ano_atual]


#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for lista in lista_numeros:
    print(lista)

#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
for lista in lista_numeros:
    if lista % 2 == 1:
        print(lista)

#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
    #Utilizando metodo reverse
for lista in reversed(lista_numeros):
    print(lista)

#Utilizando metodo de pilhas com while
while lista_numeros:
    print(lista_numeros.pop())

#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
valor = int(input('Digite um número\n'))
for i in range(1,11):
    resultado = i * valor
    print(f'{i} x {valor} = {resultado}')

#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_novos_numeros = [1,5,15]
x=0
try:
    for i in lista_novos_numeros:
        resultado = x + i
        print(resultado)
        x = resultado
except Exception as e:
    print("Erro {e}")

try:
    x = 0
    i = 0
    while i < len(lista_novos_numeros):
        x = lista_novos_numeros[i] + x
        i+= 1
    print(x)
except Exception as e:
    print(e)


#Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


lista = []
i=0
while i<3:
    valor_recebido = int(input('Digite um numero: '))
    lista.append(valor_recebido)
    i+=1

def calculo(soma,divisao):
    try:
        resultado = soma / divisao
        return print(f'A média dos 3 numeros é: {resultado}')
    except ZeroDivisionError:
        return "Erro: Não possivel dividir por zero"

soma_lista = sum(lista)
qtd_lista = len(lista)

calculo(soma_lista,qtd_lista)
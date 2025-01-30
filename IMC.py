def IMC(altura_usuario, peso_usuario):
    resultado = peso_usuario / (altura_usuario **2)
    return print(f'Seu IMC é: {resultado:.2f}')

Peso = int(input('Digite o seu peso: '))
Altura = float(input('Digite a sua altura: '))

IMC(Altura, Peso)

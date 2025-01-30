guardou = []

palavra = input("Digite a palavra chave do jogo: ").lower()
chances = int(input("Digite a quantidade de chances de erro no jogo: "))

while True:
    for letra in palavra:
        if letra in guardou:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")
    
    tentativa_usuario = input('Digite uma letra: ')
    guardou.append(tentativa_usuario.lower())

    if tentativa_usuario.lower() in palavra:
        print("Acertou!\n")
    else:
        chances -= 1
        print(f"Você agora tem {chances}\n")

    ganhou = True

    for letra in palavra:
        if letra.lower() not in guardou:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabens! Palavra {palavra}")
else: 
    print(f"Errou! Palavra {palavra}")
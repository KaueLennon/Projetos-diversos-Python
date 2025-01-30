import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo", "openai"]
    return random.choice(palavras)

def mostrar_forca(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_forca(palavra, letras_corretas))

    while tentativas < tentativas_maximas:
        letra = input("\nDigite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            letras_erradas.add(letra)
            tentativas += 1
            print(f"Letra errada! Tentativas restantes: {tentativas_maximas - tentativas}")

        print(mostrar_forca(palavra, letras_corretas))

        if "_" not in mostrar_forca(palavra, letras_corretas):
            print("\nParabéns! Você acertou a palavra!")
            break

    if tentativas == tentativas_maximas:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar_forca()
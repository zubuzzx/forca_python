import random

palavras = ["gato", "cachorro", "elefante"]

def escolher_palavra():
    return random.choice(palavras)

# Jogo da forca
def jogo_da_forca(palavra):
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        palavra_mostrada = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_mostrada += letra + " "
            else:
                palavra_mostrada += "_ "
        print(palavra_mostrada)

        if palavra_mostrada.replace(" ", "") == palavra:
            print("Parabéns! Você acertou a palavra.")
            break

        letra_jogador = input("Digite uma letra: ")

        if letra_jogador in letras_corretas or letra_jogador in letras_erradas:
            print("Você já digitou essa letra. Tente novamente.")
            continue

        if letra_jogador in palavra:
            letras_corretas.append(letra_jogador)
        else:
            letras_erradas.append(letra_jogador)
            tentativas -= 1
            print(f"Letra errada! Você tem mais {tentativas} tentativas.")

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

palavra_aleatoria = escolher_palavra()
print("Jogo da Forca")
jogo_da_forca(palavra_aleatoria)
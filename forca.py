import random


def tela_entrada_inicio_jogo():
    print("********************************")
    print("***Bem vindo ao jogo da Forca***")
    print("********************************")

def ler_arquivo_com_lista_palavras_secretas():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # tirar o \n do final da palavra dentro arquivo
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper() #limpar chute
    return chute

def marcar_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index = index + 1


def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")


def verificar_se_ja_chutou(jachutou, chutou, chute ):
    for let in chutou:
        if (chute == let):
            print("Voce ja chutou esta letra!!!!! \n")
            jachutou = True
            break

    return jachutou




def desenha_erros(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    tela_entrada_inicio_jogo()
    palavra_secreta = ler_arquivo_com_lista_palavras_secretas()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    letras_faltando = 0
    enforcou = False
    acertou = False
    erros = 0
    chutou = [""]


    #for letras in palavra_secreta:     outra maneira de iniciar o vetor letras_acertadasa
        #letras_acertadas.append("_")


    while (not enforcou and not acertou):

        jachutou = False

        if (not jachutou):
            chute = pede_chute()
            jachutou = verificar_se_ja_chutou(jachutou, chutou, chute)
        chutou.append(chute)


        if (chute in palavra_secreta):
            marcar_chute_correto(chute,letras_acertadas,palavra_secreta)

        else:

            if (not jachutou):
                erros += 1
                desenha_erros(erros)

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count("_"))
        letras_faltando_numero = int(letras_faltando)
        if (letras_faltando_numero > 0 ):
            print("Faltam [ {} ] letras para acertar a palavra\n".format(letras_faltando))
        else:
            acertou = True
            imprimir_mensagem_vencedor()

        enforcou = erros == 7
        if (enforcou):
            imprimir_mensagem_perdedor(palavra_secreta)

    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()


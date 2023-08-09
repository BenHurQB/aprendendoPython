
def escolhe_jogo():
    import forca
    import adivinhacao

    print("********************************")
    print("******Escolha o seu jogo********")
    print("********************************")



    print("[1] Forca  [2] Adivinhação")
    escolha = int(input("Sua escolha: "))
    if (escolha == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (escolha == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
if (__name__ == "__main__"):
    escolhe_jogo()
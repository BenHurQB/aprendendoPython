
def jogar():
    #  importar a bliblioteca random - números randonicos, porém vem entre 0 e 1
    import random

    print("********************************")
    print("Bem vindo ao jogo da Advinhação!")
    print("********************************")



    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print("Qaul o nível de dificuldades? ")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Defina o Nível: "))
    while(nivel < 1 or nivel > 3):
        print("[Erro] nivel de 1 a 3")
        print("(1) Fácil  (2) Médio  (3) Difícil")
        nivel = int(input("Defina o Nível: "))

    if (nivel == 1):
            total_de_tentativas = 20
    elif (nivel == 2):
            total_de_tentativas = 10
    else:
            total_de_tentativas = 5


    perdeu = 1;

    for contador in range(0,total_de_tentativas):
        print("Voce  possui {} tentativa(s)".format(total_de_tentativas - contador))
        chute_str = input("Chute o seu número entre 1 e 100:  ")
        chute = int(chute_str)
        print("Voce chutou {} ".format(chute))
        if (chute < 1 or chute>100):
            print("Voce deve digitar um número entre 1 e 100")
            continue
        acertou =  chute == numero_secreto
        maior   =  chute > numero_secreto
        menor   =  chute < numero_secreto


        if (acertou):
            print("Voce acertou o número secreto e fez [ {} ] pontos !!!".format(pontos))
            perdeu = 0
            break
        else:
            if (maior):
                    print("Voce errou!!!  O número chutado = {} é MAIOR do  que o número secreto." .format(chute))
            elif(menor):
                    print("Voce errou!!!  O número chutado = {} chute é MENOR do  que o número secreto.".format(chute))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if (perdeu):
        print("O número secreto é igual a [ {} ]. Voce PERDEU !!!!!" .format(numero_secreto))

    print("Fim do Jogo")
if (__name__ == "__main__"):
    jogar()
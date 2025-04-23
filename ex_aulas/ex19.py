from random import randint

print("🎯 Bem-vindo ao Jogo de Adivinhação!\nO computador escolheu um número entre 1 e 100.\nTente adivinhar!")

# gerando o número aleatório
num_secreto = randint(1, 100)
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < 1 or palpite > 100:
            print("⚠️ O número precisa estar entre 1 e 100.")
            continue
            #dica para o usuário + número de tentativas dele
        if palpite == num_secreto:
            print(f"🎉 Parabéns! Você acertou o número {num_secreto} em {tentativas} tentativa(s)!")
            break
        elif palpite < num_secreto:
            print("🔼 Tente um número **maior**.")
        else:
            print("🔽 Tente um número **menor**.")

    except ValueError:
        print("⚠️ Por favor, digite um número válido.")

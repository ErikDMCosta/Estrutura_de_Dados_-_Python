from random import randint

min = 0
max = 30
sorteio = randint(min, max)

while True:
    chute = randint(min, max)
    if chute == sorteio:
        print(f'Você venceu! {chute}')
        break
    else:
        if chute > sorteio:
            # print(f'O valor de chute foi {chute} e o sorteado é menor.')
            max = chute - 1
            print('Max: ', max)

        elif chute < sorteio:
            # print(f'O valor de chute foi {chute} e o sorteado é maior.')
            min = chute + 1
            print('Min: ', min)


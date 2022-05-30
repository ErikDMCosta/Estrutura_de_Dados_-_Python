from random import randint

min = 0
max = 30
sorteio = randint(min, max)

while True:
    chute = (min + max) / 2
    if chute == sorteio:
        print(f'Você venceu! {chute}')
        break
    else:
        if chute < sorteio:
            # print(f'O valor de chute foi {chute} e o sorteado é maior.')
            min = chute
            print('Min: ', min)

        elif chute > sorteio:
            # print(f'O valor de chute foi {chute} e o sorteado é menor.')
            max = chute
            print('Max: ', max)




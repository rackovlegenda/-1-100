while True:                                      # Внешний цикл (повтор игры)
    import random
    secret = random.randint(1, 100)
    attempts = 0

    while True:                                  # Внутренний цикл (угадывание)
        attempts += 1
        guess = int(input(f'Попытка {attempts}. Угадай число: '))
        if guess < secret:
            print('Больше')
        elif guess > secret:
            print('Меньше')
        elif guess == secret:
            print('В точку!')
            print(f'Ты угадал за {attempts} попыток')
            break                                # ВЫХОД ИЗ ВНУТРЕННЕГО ЦИКЛА (угадали)

    again = input('Сыграть ещё раз? (да/нет): ')  # Отступ 4 пробела
    if again == 'нет':                           # Отступ 4 пробела
        break                                    # ВЫХОД ИЗ ВНЕШНЕГО ЦИКЛА (отступ 8 пробелов)
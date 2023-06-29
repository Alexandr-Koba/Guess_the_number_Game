import random

def guess_number_game():
    secret_num = random.randint(1, 666)
    attemps = 0

    while True:
        guess = yield
        attemps += 1

        if guess < secret_num:
            print("Загаданное число больше")
        elif guess > secret_num:
            print("Загаданное число меньше")
        else:
            print(f"Поздравляю вы угадали число! {secret_num}")
            break

    print(f"Игра окончена. Вам потребовалось {attemps} попыток. ")

# Создание обьекта генератора.
game = guess_number_game()

print("Добро пожаловать в игру 'Угадай число'!")
print("Компьютер загадал число от 1 до 666")

next(game) # Запуск генератора, выполняется до первого yield.

while True:
    try:
        user_input = int(input("Введите число: "))
        game.send(user_input) # Отправка введенного числа в генератор.
    except ValueError:
        print("Ошибка! Введите число.")
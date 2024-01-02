# MineTrooper

MineTrooper - простая текстовая игра в сапёр, написанная на Python.


## Зависимости

Для запуска проекта требуется Python версии 3.x.

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/Nikolay-Yakunin/MineTrooper.git
    cd MineTrooper
    ```

2. Запустить игру:

    ```bash
    python main.py
    ```

## Использование

1. При запуске игры вам будет предложено меню с опциями.
2. Выберите опцию, введя соответствующую цифру.
3. Следуйте инструкциям для выполнения выбранной опции.

## Пример

```python
from Game import Game

# Создаем объект игры
game = Game(rows=3, columns=3, probability_mine=20, initial_balance=100)

# Отображаем доску
game.display_board()

# Открываем ячейку
game.open_cell(0, 0)

# Проверяем баланс банка
print(f"Your current bank balance is: {game.get_bank_balance()}")
```

## Автор

Nikolay-Yakunin

## Лицензия

MIT

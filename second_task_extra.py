from second_task import GamePole

def play_minesweeper():
    """Интерактивная игра в сапер"""
    # Создаем игровое поле 8x8 с 10 минами
    game = GamePole(8, 10)
    
    while True:
        # Показываем текущее состояние поля
        print("\nИгровое поле:")
        game.show()
        
        # Запрашиваем координаты
        try:
            move = input("\nВведите координаты клетки через пробел (строка столбец) или q для выхода: ")
            
            if move.lower() == 'q':
                print("Игра завершена!")
                break
                
            row, col = map(int, move.split())
            
            # Проверяем корректность координат
            if not (0 <= row < 8 and 0 <= col < 8):
                print("Координаты должны быть от 0 до 7!")
                continue
                
            # Открываем клетку
            cell = game.pole[row][col]
            cell.is_open = True
            
            # Проверяем, не попали ли мы в мину
            if cell.is_mine:
                print("\nБУМ! Вы попали на мину. Игра окончена!")
                # Открываем все клетки
                for i in range(8):
                    for j in range(8):
                        game.pole[i][j].is_open = True
                print("\nПоле целиком:")
                game.show()
                break
                
        except (ValueError, IndexError):
            print("Некорректный ввод! Введите два числа от 0 до 7, разделенные пробелом.")
            continue


if __name__ == "__main__":
    print("Добро пожаловать в игру Сапер!")
    print("Используйте координаты от 0 до 7 для открытия клеток.")
    print("Символы на поле:")
    print("# - закрытая клетка")
    print("* - мина")
    print("0-8 - количество мин вокруг клетки")
    print()
    
    play_minesweeper()
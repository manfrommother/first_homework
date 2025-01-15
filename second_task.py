from random import randint
from typing import List


class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, value: bool):
        self.__is_mine = value

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value: int):
        self.__number = value

    @property
    def is_open(self):
        return  self.__is_open
    
    @is_open.setter
    def is_open(self, value: bool):
        self.__is_open = value
    

class GamePole:
    
    def __init__(self, N: int, M: int):
        '''
        Инициализация игрового поля

        Args:
        N(int): размер поля NxN
        M(int): общее число мин на карте
        '''
        self.__N = N
        self.__M = M
        self.__pole = self.init()

    @property
    def pole(self) -> List[List[Cell]]:
        return self.__pole
    
    def init(self) -> List[List[Cell]]:
        '''Инициализация поля с новой расстановкой мин'''
        pole = [[Cell() for _ in range(self.__N)] for _ in range(self.__N)]

        # Расставляем мины в случайном порядке
        m = 0
        while m < self.__M:
            i = randint(0, self.__N - 1)
            j = randint(0, self.__N - 1)
            if not pole[i][j].is_mine:
                pole[i][j].is_mine = True
                m += 1
        # Вычисляем количеств омин вокруг каждой клетки
        for i in range(self.__N):
            for j in range(self.__N):
                if not pole[i][j].is_mine:
                    self.__count_mines_around(pole, i, j)

        return pole
    
    def __count_mines_around(self, pole: List[List[Cell]], i: int, j: int):
        '''Подсчет количества мин вокруг клетки (i, j)'''
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < self.__N and 0 <= nj < self.__N and pole[ni][nj].is_mine:
                    count += 1
        pole[i][j].number = count

    def show(self):
        '''Отображение поля в консоли'''
        for i in range(self.__N):
            for j in range(self.__N):
                cell = self.__pole[i][j]
                if cell.is_open:
                    print('*' if cell.is_mine else cell.number, end=' ')
                else:
                    print('#', end=' ')
            print()

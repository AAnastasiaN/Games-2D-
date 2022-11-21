import pygame
# отслеживание статистики
class Stats():
    def __init__(self):
    # инициализирует статистику
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
    # статистика изменяющаяся во время игры
        self.guns_left = 2
        self.score = 0

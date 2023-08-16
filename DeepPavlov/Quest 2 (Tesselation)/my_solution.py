import random
import test_solution

class KnightsTour:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.board = self._get_board()
        self.route = []

    def _get_board(self) -> dict[tuple: int]:
        """
        инициализируем доску
        """
        board = {}
        for x in range(self.n):
            for y in range(self.m):
                board.update({(x, y): 0})
        return board

    def _is_safe(self, coordinate: tuple[int, int]) -> bool:
        """
        проверка заданных координат на корректность
        """
        if 0 <= coordinate[0] < self.n and 0 <= coordinate[1] < self.m:
            return True
        return False

    def _get_possible_steps(self, coords: tuple[int, int]) -> list[tuple[int, int]]:
        """
        функция рассчета возможных ходов коня из текущей позиции (на основе всех возможных ходов, которые конь по правилам шахмат может сделать)
        """
        possible_steps = []
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for move in moves:
            x_new = coords[0] + move[0]
            y_new = coords[1] + move[1]
            if self._is_safe((x_new, y_new)):
                possible_steps.append((x_new, y_new))
        return possible_steps

    def solve_knights(self) -> list[list, ...]:
        """
        функция зачеркивающая совершенные ходы.

        стартовая точка коня - левая нижняя клетка на доске = (0,0).
        функция будет работать до тех пор, пока конь не наступит на каждую клетку.
        """
        start = (0, 0)
        self.board.update({start: self.board.get(start)})
        current = start
        self.route.append(list(current))
        iteration = 1
        last = None
        while 0 in self.board.values():  # while board contains zero-tiles
            iteration += 1
            # possible steps - это список ходов, которые конь может совершить
            possible_steps = self._get_possible_steps(current)

            flag_one_step = False  

            for possible_step in possible_steps:
                if self.board[possible_step] == 0:
                    last = current
                    current = possible_step
                    self.route.append(list(current))
                    self.board[current] += 1
                    flag_one_step = True

                    break
            #  если мы не можем найти шаг коня, который закрыл бы клетку, ставим коня в случайное положение
            if not flag_one_step:
                #  проверим есть ли возможность закрыть клетку в 2 шага
                flag_two_steps = False

                # проходимся по незакрытым клеткам
                for coord, steps in self.board.items():
                    if steps == 0:  
                        #  ищем пересечения между  нынешним положением и положением нужной клетки
                        one_step_to_zero_tile = set(self._get_possible_steps(coord)) & set(possible_steps)
                        # если найдено хотя бы одно такое пересечение, конь находит путь к клетке
                        if one_step_to_zero_tile:
                            last = current
                            current = one_step_to_zero_tile.pop()
                            flag_two_steps = True
                            break
                # если конь не нашел способ за два хода добраться до цели - он идет в случайном направлении
                if not flag_two_steps:
                    if last:
                        possible_steps.remove(last)
                    last = current
                    current = possible_steps[random.randint(0, len(possible_steps) - 1)]

                self.route.append(list(current))
                self.board[current] += 1
        print(iteration)
        return self.route


def main(desk_size: list):
    return KnightsTour(desk_size[0], desk_size[1]).solve_knights()


if __name__ == "__main__":
     score = test_solution.evaluate_task([5, 5], main)
     print(f"task {score=}")
     print(main([9,10]))
    # main([5,5])

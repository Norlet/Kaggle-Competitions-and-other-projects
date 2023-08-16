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
        Method initializes a board with set parameters (n x m)
        :return: board with structure {tile coordinates: count of steps}
        """
        board = {}
        for x in range(self.n):
            for y in range(self.m):
                board.update({(x, y): 0})
        return board

    def _is_safe(self, coordinate: tuple[int, int]) -> bool:
        """
        Checks if coordinate meets the condition to be within the board.
        This method is required to
        :param coordinate:
        :return: True if coordinates fits condition and False if it doesn't
        """
        if 0 <= coordinate[0] < self.n and 0 <= coordinate[1] < self.m:
            return True
        return False

    def _get_possible_steps(self, coords: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Compute all the possible ways that knight may step on the board.
        :param coords: current coordinate of the knight
        :return: possible_steps: list of all the possible coordinates of the steps
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
        Tile all the cells of board by moves of knight(chess).

        Start point of knight is lower left corner - start = (0,0).
        The body of function works until the board contains tiles that had no foot of knight on it (these
        tiles we will call `zero-tiles`).

        :return: path-list of knight's moves
        """
        start = (0, 0)
        self.board.update({start: self.board.get(start)})
        current = start
        self.route.append(list(current))
        iteration = 1
        last = None
        while 0 in self.board.values():  # while board contains zero-tiles
            iteration += 1
            # possible steps is the list that contains all the steps that knight may go
            possible_steps = self._get_possible_steps(current)

            flag_one_step = False  # flag signals if there are one-step way to reduce zero-tiles

            # as soon as we meet the step that close one zero-tile we stop (by `break`) iteration of possible paths
            # and step onto first encountered-tile
            for possible_step in possible_steps:
                if self.board[possible_step] == 0:
                    last = current
                    current = possible_step
                    self.route.append(list(current))
                    self.board[current] += 1
                    flag_one_step = True

                    break
            #  if we couldn't find a step that close the zero-tile we put the knight into random possible tile
            if not flag_one_step:
                #  check if there are two-step ways to zero-tile. flag_two_steps shows if it is available
                flag_two_steps = False

                # iterating through zero-tiles on board
                for coord, steps in self.board.items():
                    if steps == 0:  # check if it zero-tile
                        #  we look up for intersections between moves of zero-tile and current site
                        one_step_to_zero_tile = set(self._get_possible_steps(coord)) & set(possible_steps)
                        # if found at least one such intersection knight go there and next move knight will find true
                        # way
                        if one_step_to_zero_tile:
                            last = current
                            current = one_step_to_zero_tile.pop()
                            flag_two_steps = True
                            break
                # if knight hasn't found two-step ways he goes in a random way (random index from possible_ways)
                if not flag_two_steps:
                    # remove extra repeat by removing from possible steps last tile
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

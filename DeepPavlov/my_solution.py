def knight_move(i: int, j: int, pos: int, board: list[list[int, int]], result: list, moves: list[tuple], height: int,
                width: int):
    board[i][j] = pos
    result.append([i, j])
    while not all([item for elem in board for item in elem]):
        for mi, mj in moves:
            x_1 = i + mi
            y_1 = j + mj
            if 0 <= x_1 < height and 0 <= y_1 < width:
                if board[x_1][y_1] == 0:
                    pos += 1
                    board[x_1][y_1] = pos
                    result.append([x_1, y_1])
                    i, j = x_1, y_1
                    continue
        for mi, mj in moves:
            x_1 = i + mi
            y_1 = j + mj
            if 0 <= x_1 < height and 0 <= y_1 < width:
                pos += 1
                board[x_1][y_1] = pos
                result.append([x_1, y_1])
                i, j = x_1, y_1
                break

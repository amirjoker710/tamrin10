import numpy as np


class sudoku():

    def __init__(self):
        self.board = np.zeros((9, 9), dtype=int)  # start with blank board
        self.__fill_cell(0)
        self.test1 = 0
        self.test2 = 0

    def __fill_cell(self, k):
        if k == 81:
            return True
        i = k // 9
        j = k % 9

        row = set(self.board[i, :])
        column = set(self.board[:, j])
        square = set(self.board[(i // 3) * 3:(1 + i // 3) * 3, (j // 3) * 3:(1 + j // 3) * 3].flatten())
        usedNumSet = row.union(column).union(square)
        # pick a number for cell (i,j) from the set of remaining available numbers
        choices = list(set(range(1, 10)).difference(usedNumSet))
        np.random.shuffle(choices)
        for choice in choices:
            self.board[i, j] = choice
            if self.__fill_cell(k + 1):
                return True
        self.board[i, j] = 0
        return False

    def get_puzzle(self, n=20):
        mask = np.array([0] * n + [1] * (81 - n), dtype=int)
        np.random.shuffle(mask)
        return mask.reshape(9, 9) * self.board

    # issue = get_puzzle()
    def get_solution(self, issue):
        mask = np.array([0] * 81, dtype=int)
        mask.reshape(9, 9)
        for i in range(0, 9):
            for j in range(0, 9):
                if issue[i, j] == 0:
                    mask[i, j] = 0
                else:
                    mask[i, j] = 1
        for i in range(0, 9):
            for j in range(0, 9):
                if mask[i, j] == 1:
                    continue
                else:
                    row = set(self.board[i, :])
                    column = set(self.board[:, j])
                    square = set(self.board[(i // 3) * 3:(1 + i // 3) * 3, (j // 3) * 3:(1 + j // 3) * 3].flatten())
                    usedNumSet = row.union(column).union(square)
                    choices = list(set(range(1, 10)).difference(usedNumSet))
                    for choice in choices:
                        issue[i, j] = choice
                    return self.board[i, j]

    def get_solution(self):#printing all answers
        print(self.board)
        while get_solution(self, issue) != 10:
            i=0
            print("number :", i + 1)
            get_solution(self.board)



mysudoku = sudoku()

print("puzzle:")
print(mysudoku.get_puzzle())

mysudoku.get_solution()



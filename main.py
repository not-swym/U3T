class U3T:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]  # 0 is empty, -1 is opponent, 1 is player

        self.current_local_board = 5
        self.current_player = 1

    def possible_moves(self, sub_board, player):  # lists all possible moves in a sub-board
        possible = []
        for i in range(len(self.board[sub_board])):
            if self.board[sub_board][i] == 0 and self.board[sub_board][i] != player:
                possible.append(i)
        return possible

    def move(self, sub_board, cell, player):  # check if move is legal make move and returns current player, sub-board
        if self.current_local_board == sub_board and self.current_player == player:
            if cell in self.possible_moves(sub_board, player):
                self.board[sub_board][cell] = player

        return [(1 if player == -1 else -1), cell]

    def sub_board_won(self, sub_board, player):  # checks if a sub-board is won or in-progress and returns bool
        rows = self.board[sub_board]
        cols = [self.board[i][sub_board] for i in range(9)]
        diagonal_1 = [self.board[i][i] for i in range(9) if i % 10 == 0]
        diagonal_2 = [self.board[i][j] for i, j in zip(range(8, -1, -1), range(9)) if i != 4]

        win_conditions = [rows, cols, diagonal_1, diagonal_2]

        for condition in win_conditions:
            if condition.count(player) == 3:
                return True
        return False

    def is_draw(self, sub_board):  # checks if a sub-board is drawn and returns boolean
        return (all(cell != 0 for cell in self.board[sub_board])
                and not self.sub_board_won(sub_board, 1)
                and not self.sub_board_won(sub_board, -1))

        # set the drawn sub_board to a value that indicates drawn

    def game_over(self):  # checks if the game is won and returns [-1, 0, 1] => [lost, draw, won]
        for i in range(9):
            if self.sub_board_won(i, 1) or self.sub_board_won(i, -1):
                return 1
        # add a scenario where the game is drawn
        return -1

    def update(self, sub_board):
        if self.sub_board_won(self.board[sub_board], self.current_player):
            for cell in range(9):
                self.board[sub_board][cell] = self.current_player


# NOTE: Call update after every move, and update the current_local_board and current_player from the
# return value of self.move

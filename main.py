import copy

class uttt:
    def __init__(self) -> None:
        self.current_player = 1
        self.current_board = None
        self.possible_moves = []
        self.sub_board_state = [0 for _ in range(9)]
        self.game_state = False
        self.make_board()

    def make_board(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def find_possible_moves(self, sub_board):
        self.possible_moves = []
        for cell in range(9):
            if self.board[sub_board][cell] == 0:
                self.possible_moves.append((cell, sub_board))

        if not self.possible_moves:
            for subboard in range(9):
                for cell in range(9):
                    if self.board[subboard][cell] == 0:
                        self.possible_moves.append((cell, subboard))

    def move(self, sub_board, cell):
        if (cell, sub_board) in self.possible_moves:
            new_board = copy.deepcopy(self.board)
            if new_board[sub_board][cell] == 0:
                new_board[sub_board][cell] = self.current_player
                new_current_player = 1 if self.current_player == -1 else -1
                new_current_board = cell
                new_sub_board_state = [self.current_player if self.check_win(new_board[sub_board]) else 0 for sub_board in range(9)]
                return new_board, new_current_player, new_current_board, new_sub_board_state
        return None, None, None, None

    def apply_move(self, new_board, new_current_player, new_current_board, new_sub_board_state):
        if new_board:
            self.board = new_board
            self.current_player = new_current_player
            self.current_board = new_current_board
            self.sub_board_state = new_sub_board_state

    def check_win(self, state):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combo in winning_combinations:
            if all(state[i] == self.current_player for i in combo):
                return True
        return False # This means the game is draw or in progress 
        

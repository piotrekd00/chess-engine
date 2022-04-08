from random import randint
from figures import Queen, Pawn


class GenerateBoard:

    def __init__(self, n):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] for _ in range(0, 8)]
        self.num_queens = n
        self.queens_list = []
        self.pawn = str
        if isinstance(n, int):
            if n <= 0:
                raise ValueError("Number of queens must be bigger than 0!")
            elif n >= 64:
                raise ValueError("Number of queens must be smaller than 64!")
        else:
            raise TypeError("Number of queens must be a type of int")

    def get_pawn(self):
        self.pawn = Pawn(randint(0, 7), randint(0, 7))
        self.board[self.pawn.pos_x][self.pawn.pos_y] = self.pawn.symbol

    def get_queens(self):
        self.get_pawn()
        for x in range(self.num_queens):
            queen = Queen(x+1, randint(0, 7), randint(0, 7))
            while not self.board[queen.pos_x][queen.pos_y] == ' ':
                queen = Queen(x + 1, randint(0, 7), randint(0, 7))
            self.queens_list.append(queen)
            self.board[queen.pos_x][queen.pos_y] = queen.symbol

    def draw_board(self):
        for row in self.board:
            print(row)

    def get_new_pawn(self):
        self.board[self.pawn.pos_x][self.pawn.pos_y] = ' '
        self.pawn = Pawn(randint(0, 7), randint(0, 7))
        while not self.board[self.pawn.pos_x][self.pawn.pos_y] == ' ':
            self.pawn = Pawn(randint(0, 7), randint(0, 7))
        self.board[self.pawn.pos_x][self.pawn.pos_y] = self.pawn.symbol

    def pop_queen(self, queen_id):
        if queen_id <= 0 or queen_id > len(self.queens_list):
            raise ValueError("Enter correct queen's id!")
        self.board[self.queens_list[queen_id-1].pos_x][self.queens_list[queen_id-1].pos_y] = ' '
        self.queens_list.pop(queen_id-1)

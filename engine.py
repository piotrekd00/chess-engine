from board import GenerateBoard


class Engine:

    def __init__(self, n):
        self.game = GenerateBoard(n)
        self.game.get_queens()

    def beat_check(self):
        q = {'lu': False, 'ld': False, 'rd': False, 'ru': False, 'u': False, 'd': False, 'l': False, 'r': False}
        for i in range(0, 8):

            try:

                if self.game.pawn.pos_y - i >= 0 and not q['l']:
                    pos1l = self.game.board[self.game.pawn.pos_x][self.game.pawn.pos_y - i]
                    if pos1l == 'Q':
                        self.get_queen_pos(self.game.pawn.pos_x, self.game.pawn.pos_y - i)
                        q['l'] = True

                if self.game.pawn.pos_y + i <= 7 and not q['r']:
                    pos1r = self.game.board[self.game.pawn.pos_x][self.game.pawn.pos_y + i]
                    if pos1r == 'Q':
                        self.get_queen_pos(self.game.pawn.pos_x, self.game.pawn.pos_y + i)
                        q['r'] = True

                if self.game.pawn.pos_x + i <= 7 and not q['d']:
                    pos1u = self.game.board[self.game.pawn.pos_x + i][self.game.pawn.pos_y]
                    if pos1u == 'Q':
                        self.get_queen_pos(self.game.pawn.pos_x + i, self.game.pawn.pos_y)
                        q['d'] = True

                if self.game.pawn.pos_x - i >= 0 and not q['u']:
                    pos1d = self.game.board[self.game.pawn.pos_x - i][self.game.pawn.pos_y]
                    if pos1d == 'Q':
                        self.get_queen_pos(self.game.pawn.pos_x - i, self.game.pawn.pos_y)
                        q['u'] = True

            except IndexError:
                pass

            if self.game.pawn.pos_x - i >= 0 and self.game.pawn.pos_y - i >= 0 and not q["lu"]:
                pos3 = self.game.board[self.game.pawn.pos_x - i][self.game.pawn.pos_y - i]
                if pos3 == 'Q':
                    self.get_queen_pos(self.game.pawn.pos_x - i, self.game.pawn.pos_y - i)
                    q["lu"] = True

            if self.game.pawn.pos_x + i <= 7 and self.game.pawn.pos_y + i <= 7 and not q["rd"]:
                pos4 = self.game.board[self.game.pawn.pos_x + i][self.game.pawn.pos_y + i]
                if pos4 == 'Q':
                    self.get_queen_pos(self.game.pawn.pos_x + i, self.game.pawn.pos_y + i)
                    q["rd"] = True

            if self.game.pawn.pos_x + i <= 7 and self.game.pawn.pos_y - i >= 0 and not q["ru"]:
                pos5 = self.game.board[self.game.pawn.pos_x + i][self.game.pawn.pos_y - i]
                if pos5 == 'Q':
                    self.get_queen_pos(self.game.pawn.pos_x + i, self.game.pawn.pos_y - i)
                    q["ru"] = True

            if self.game.pawn.pos_x - i >= 0 and self.game.pawn.pos_y + i <= 7 and not q["ld"]:
                pos6 = self.game.board[self.game.pawn.pos_x - i][self.game.pawn.pos_y + i]
                if pos6 == 'Q':
                    self.get_queen_pos(self.game.pawn.pos_x - i, self.game.pawn.pos_y + i)
                    q["ld"] = True
        print(q)

    def get_queen_pos(self, x, y):
        for queen in self.game.queens_list:
            if queen.pos_x == x and queen.pos_y == y:
                print("Hetman o id: {} ma bicie z pozycji {} {}".format(queen.id, y+1, x+1))

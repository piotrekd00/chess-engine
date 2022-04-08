from engine import Engine


def main():
    board = Engine(5)
    board.game.draw_board()
    board.beat_check()
    board.game.get_new_pawn()
    board.game.draw_board()
    board.beat_check()
    board.game.pop_queen(2)
    board.game.draw_board()
    board.beat_check()


if __name__ == '__main__':
    main()

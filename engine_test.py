import unittest
import chess


class TestQueenNum(unittest.TestCase):

    def test_if_null(self):
        self.assertRaises(ValueError, chess.Engine, 0)

    def test_if_negative(self):
        self.assertRaises(ValueError, chess.Engine, -1)

    def test_if_too_big(self):
        self.assertRaises(ValueError, chess.Engine, 64)

    def test_if_not_int(self):
        self.assertRaises(TypeError, chess.Engine, 'd')
        self.assertRaises(TypeError, chess.Engine, 1.5)
        self.assertRaises(TypeError, chess.Engine, -1.5)


class TestQueenPop(unittest.TestCase):

    def setUp(self):
        self.case = chess.Engine(5)

    def test_if_null(self):
        self.assertRaises(ValueError, self.case.game.pop_queen, 0)

    def test_if_negative(self):
        self.assertRaises(ValueError, self.case.game.pop_queen, -2)

    def test_if_too_big(self):
        self.assertRaises(ValueError, self.case.game.pop_queen, 6)


if __name__ == '__main__':
    unittest.main()

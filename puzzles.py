import random
import chess

PUZZLES = [
    # Each puzzle is a FEN and the best move for White
    ("r1bqkbnr/pppppppp/n7/8/1P6/5N2/P1PPPPPP/RNBQKB1R b KQkq - 1 2", "a6b4"),
    ("r2q1rk1/pp2bppp/1nn1p3/2ppP3/3P4/2P1BN2/PP3PPP/RNBQ1RK1 w - - 0 9", "f3d2"),
    ("r4rk1/ppp2ppp/2n2n2/3q4/3P4/2N1PN2/PPQ2PPP/R3KB1R w KQ - 3 11", "c3xd5"),
]


def random_puzzle():
    fen, move = random.choice(PUZZLES)
    board = chess.Board(fen)
    return board, chess.Move.from_uci(move)


def show_puzzle():
    board, solution = random_puzzle()
    print(board)
    guess = input("Your move (UCI): ")
    if guess == solution.uci():
        print("Correct!")
    else:
        print(f"Wrong. Solution is {solution}")

if __name__ == "__main__":
    show_puzzle()

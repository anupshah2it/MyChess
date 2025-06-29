import chess
import chess.engine
import sys
from pathlib import Path
from rating import load_players, record_result

STOCKFISH_PATH = "/usr/games/stockfish"


def play_game(player_name):
    board = chess.Board()
    players = load_players()
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

    try:
        while not board.is_game_over():
            print(board)
            if board.turn == chess.WHITE:
                move_str = input("Your move (in UCI, e.g. e2e4): ")
                try:
                    move = chess.Move.from_uci(move_str)
                except ValueError:
                    print("Invalid move format. Try again.")
                    continue
                if move not in board.legal_moves:
                    print("Illegal move. Try again.")
                    continue
                board.push(move)
            else:
                result = engine.play(board, chess.engine.Limit(time=0.1))
                board.push(result.move)
                print(f"Engine plays: {result.move}")
    finally:
        engine.quit()

    print(board)
    result = board.result()
    print("Game over:", result)

    if result == "1-0":
        record_result(players, player_name, "engine", 1)
    elif result == "0-1":
        record_result(players, player_name, "engine", 0)
    else:
        record_result(players, player_name, "engine", 0.5)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python chess_game.py <player_name>")
        sys.exit(1)
    play_game(sys.argv[1])

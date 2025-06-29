import chess
import chess.engine
from flask import Flask, request, jsonify, send_from_directory
from rating import load_players, save_players, ensure_player, use_token

STOCKFISH_PATH = "/usr/games/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json(force=True)
    player = data.get("player", "guest")
    fen = data.get("fen")
    move_uci = data.get("move")
    if not fen or not move_uci:
        return jsonify({"error": "missing parameters"}), 400
    board = chess.Board(fen)
    try:
        move = chess.Move.from_uci(move_uci)
    except ValueError:
        return jsonify({"error": "invalid move"}), 400
    if move not in board.legal_moves:
        return jsonify({"error": "illegal move"}), 400
    players = load_players()
    ensure_player(players, player)
    if not use_token(players, player):
        save_players(players)
        return jsonify({"error": "out of tokens"}), 402
    board.push(move)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    save_players(players)
    return jsonify({"engine_move": result.move.uci(), "fen": board.fen()})

@app.route("/analysis", methods=["POST"])
def analysis():
    data = request.get_json(force=True)
    player = data.get("player", "guest")
    fen = data.get("fen")
    if not fen:
        return jsonify({"error": "missing fen"}), 400
    board = chess.Board(fen)
    players = load_players()
    ensure_player(players, player)
    if not use_token(players, player):
        save_players(players)
        return jsonify({"error": "out of tokens"}), 402
    info = engine.analyse(board, chess.engine.Limit(depth=12))
    best = info["pv"][0]
    score = info["score"].white().score(mate_score=10000)
    save_players(players)
    return jsonify({"best_move": best.uci(), "score": score})

if __name__ == "__main__":
    app.run(debug=True)

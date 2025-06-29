import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("players.json")


def load_players():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_players(players):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2)


def update_elo(rating_a, rating_b, result, k=32):
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    expected_b = 1 - expected_a
    new_a = rating_a + k * (result - expected_a)
    new_b = rating_b + k * ((1 - result) - expected_b)
    return round(new_a), round(new_b)


def ensure_player(players, name):
    players.setdefault(name, {
        "rating": 1200,
        "history": [],
        "tokens": 10,
        "premium": False,
    })


def use_token(players, name):
    player = players.get(name)
    if not player:
        ensure_player(players, name)
        player = players[name]
    if player.get("premium"):
        return True
    if player.get("tokens", 0) > 0:
        player["tokens"] -= 1
        return True
    return False


def record_result(players, player_a, player_b, result):
    # result: 1 if A wins, 0 if B wins, 0.5 draw
    ensure_player(players, player_a)
    ensure_player(players, player_b)

    rating_a = players[player_a]["rating"]
    rating_b = players[player_b]["rating"]

    new_a, new_b = update_elo(rating_a, rating_b, result)
    players[player_a]["rating"] = new_a
    players[player_b]["rating"] = new_b

    now = datetime.utcnow().isoformat()
    players[player_a]["history"].append({"time": now, "rating": new_a})
    players[player_b]["history"].append({"time": now, "rating": new_b})

    save_players(players)


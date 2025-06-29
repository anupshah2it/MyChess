# MyChess

MyChess provides a simple online chess experience with integrated AI analysis. It uses [python-chess](https://github.com/niklasf/python-chess) and the Stockfish engine.

## Features

- **Play vs Engine**: Web interface to play against Stockfish.
- **Rating Tracking**: Player ratings are updated using the ELO algorithm after each game. Ratings, token counts and premium status are stored in `players.json`.
- **Puzzles**: Run `python puzzles.py` to get a random tactical puzzle.
- **Analysis API**: Submit positions for engine analysis using `/analysis`.

## Requirements

- Python 3.12+
- `python-chess` library
- `Flask` web framework
- Stockfish engine available in your PATH

Install dependencies with:

```bash
pip install flask python-chess
sudo apt-get install stockfish
```

## Usage

Run the web server and open `http://localhost:5000` in your browser:

```bash
python app.py
```

Solve a random puzzle from the command line:

```bash
python puzzles.py
```

Player ratings, token usage and history are stored in `players.json`.

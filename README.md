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

## Installation

### Linux

Install Python 3.12 or newer and run:

```bash
sudo apt-get install stockfish
pip install flask python-chess
```

The engine binary is typically available at `/usr/games/stockfish`, which is the
default path used in the code.

### Windows

1. Install [Python](https://www.python.org/downloads/) and make sure `pip` is on
   your PATH.
2. Install the required libraries:

   ```bash
   pip install flask python-chess
   ```
3. Download a Stockfish build for Windows from <https://stockfishchess.org/> or
   install it via a package manager such as Chocolatey:

   ```powershell
   choco install stockfish
   ```
4. Update the `STOCKFISH_PATH` constant in `app.py` and `chess_game.py` to
   point to the location of `stockfish.exe` (e.g. `C:\\Program Files\\Stockfish\\stockfish.exe`).

Use `py` instead of `python` if your system registers the Python launcher.

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

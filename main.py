import chess
import chess.engine

# Start the Stockfish engine
engine = chess.engine.SimpleEngine.popen_uci(".\\stockfish_15.1_win_x64_avx2\\stockfish-windows-2022-x86-64-avx2.exe")

# Create a chess board
board = chess.Board()

# Get user's skill level
level = input("Select your skill level (1-5): ")
try:
    level = int(level)
    if level < 1 or level > 5:
        raise ValueError
except ValueError:
    print("Invalid skill level")
    level = 1

while not board.is_game_over():
    # Get user's move
    user_move = input("Enter your move (in UCI format, e.g. e2e4): ")
    try:
        # Try to execute the move
        move = chess.Move.from_uci(user_move)
        if board.is_legal(move):
            board.push(move)
        else:
            print("Invalid move")
            continue
    except:
        print("Invalid move")
        continue

    # Use the Stockfish engine to suggest a move
    time_limit = 5 - level
    info = engine.play(board, chess.engine.Limit(time=time_limit))
    pc_move = info.move
    board.push(pc_move)
    print("PC move:", pc_move)

# Print the result of the game
result = board.result()
if result == "1-0":
    print("You won!")
elif result == "0-1":
    print("You lost!")
else:
    print("It's a draw!")

# Quit the engine
engine.quit()

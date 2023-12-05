 
from flask import Flask, render_template, request

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    # Get the player's move
    move = request.form.get('move')

    # Update the game board
    game_board[move] = 'X'

    # Check for a winner
    winner = check_winner()

    # If there is a winner, redirect to the winner page
    if winner:
        return render_template('winner.html', winner=winner)

    # If the game is a tie, redirect to the tie page
    if is_tie():
        return render_template('tie.html')

    # Otherwise, return to the index page
    return render_template('index.html')

@app.route('/reset')
def reset():
    # Reset the game board
    game_board = {'1': ' ', '2': ' ', '3': ' ',
                   '4': ' ', '5': ' ', '6': ' ',
                   '7': ' ', '8': ' ', '9': ' '}

    # Redirect to the index page
    return render_template('index.html')

# Helper functions
def check_winner():
    # Check for a winner in the rows
    for row in range(1, 4):
        if game_board[str(row*3-2)] == game_board[str(row*3-1)] == game_board[str(row*3)] == 'X':
            return 'X'
        elif game_board[str(row*3-2)] == game_board[str(row*3-1)] == game_board[str(row*3)] == 'O':
            return 'O'

    # Check for a winner in the columns
    for col in range(1, 4):
        if game_board[str(col)] == game_board[str(col+3)] == game_board[str(col+6)] == 'X':
            return 'X'
        elif game_board[str(col)] == game_board[str(col+3)] == game_board[str(col+6)] == 'O':
            return 'O'

    # Check for a winner in the diagonals
    if game_board['1'] == game_board['5'] == game_board['9'] == 'X':
        return 'X'
    elif game_board['1'] == game_board['5'] == game_board['9'] == 'O':
        return 'O'
    if game_board['3'] == game_board['5'] == game_board['7'] == 'X':
        return 'X'
    elif game_board['3'] == game_board['5'] == game_board['7'] == 'O':
        return 'O'

    # No winner
    return None

def is_tie():
    # Check if all squares are filled
    for square in game_board.values():
        if square == ' ':
            return False

    # Tie game
    return True

# Main
if __name__ == '__main__':
    app.run(debug=True)

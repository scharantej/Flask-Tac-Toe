 # Design for TicTacToe Flask Application

## HTML Files

* `index.html`: This will be the main page of the application. It will contain the game board and the buttons for players to make their moves.
* `winner.html`: This page will be displayed when a player wins the game. It will show the winning player's name and the winning combination.
* `tie.html`: This page will be displayed when the game ends in a tie. It will show the message "Tie game!"

## Routes

* `/`: This route will render the `index.html` file.
* `/move`: This route will handle the player's moves. It will update the game board and check for a winner. If there is a winner, it will redirect to the `winner.html` page. If the game is a tie, it will redirect to the `tie.html` page.
* `/reset`: This route will reset the game board and start a new game.

## Application Flow

The application flow is as follows:

1. The user opens the application in their browser.
2. The `/` route is triggered and the `index.html` file is rendered.
3. The user clicks on a square on the game board.
4. The `/move` route is triggered and the game board is updated.
5. The game board is checked for a winner.
6. If there is a winner, the `winner.html` page is rendered.
7. If the game is a tie, the `tie.html` page is rendered.
8. The user can click the "Reset" button to start a new game.
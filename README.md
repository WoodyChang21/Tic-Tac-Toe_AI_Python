# Tic-Tac-Toe_AI

This Tic-Tac-TOE AI is an undefeatable AI that has certain logic to identify the best move to win the game or to prevent from losing.

## AI LOGIC

### 1. Check for AI win move
It detects the winning condition of AI. If AI has the possibliity of winning, AI will win directly.

### 2. Check for Player win move
If AI doesn't have the possibility of winning in the next move, AI will check if the player is winning in the next move and block the position

### 3. Check for AI Fork opportunity
Fork situation is when the player/AI has two condition of winning, which is usually a "Chekc Mate" in the Tic-tac-toe. If AI has the opportunity of having a Fork situation, AI will take that move.

### 4. Check for player Fork opporutnity
If the player have only one position to form a Fork situation, AI will block that position. However, if the player has two positions to form a Fork situation, AI will force the player to block AI and that blocking position won't be on the forming Fork position.

### 5. Check Center
If all the conditions above didn't happen, take the center if the center is not occupied.

### 6. Check Corners
If Center is occupied, take the corner if the corner is not occupied.

### 7. Check Sides
Take the sides if both center and corners are occupied.

## Display
<img width="63" alt="image" src="https://user-images.githubusercontent.com/99929453/198904407-1aaafb86-4c81-415f-92ff-900b10160a8b.png">
It will be radomly chosen for who goes first.
The player will be asked choose either "X" or "O"
The player will then be asked to input the position they want to take.




# Tic-Tac-Toe_AI

This Tic-Tac-TOE AI is an undefeatable AI that has a certain logic to identify the best move to win the game or to prevent from losing.
This project has been built in pygame library which provides user interface to interact with the AI

## AI LOGIC

### 1. Check for AI win move
It detects the winning condition of AI. If AI has the possibliity of winning, AI will win directly.

<img width="200" alt="image" src="https://user-images.githubusercontent.com/99929453/208484972-a240dc4c-b5ea-4b52-88de-8b046ed0c804.png">

### 2. Check for Player win move
If AI doesn't have the possibility of winning in the next move, AI will check if the player is winning in the next move and block the position

<img width="200" alt="image" src="https://user-images.githubusercontent.com/99929453/208484989-8892cafb-7ef5-491c-962e-7e8a7cd04cad.png">

### 3. Check for AI Fork opportunity
Fork situation is when the player/AI has two condition of winning, which is usually a "Chekc Mate" in the Tic-tac-toe. If AI has the opportunity of having a Fork situation, AI will take that move.

<img width="198" alt="image" src="https://user-images.githubusercontent.com/99929453/208485214-2964a3a2-a6d8-4fd2-93b9-5336f50f5b96.png">

### 4. Check for player Fork opporutnity
If the player have only one position to form a Fork situation, AI will block that position. However, if the player has two positions to form a Fork situation, AI will force the player to block AI and that blocking position won't be on the forming Fork position.

<img width="198" alt="image" src="https://user-images.githubusercontent.com/99929453/208485285-b25c96ee-6967-48f6-ada8-4352a83f5ced.png">

### 5. Check Center
If all the conditions above didn't happen, take the center if the center is not occupied.

### 6. Check Corners
If Center is occupied, take the corner if the corner is not occupied.

### 7. Check Sides
Take the sides if both center and corners are occupied.

## Overall
This function concludes the AI's final position

<img width="284" alt="image" src="https://user-images.githubusercontent.com/99929453/208487316-076fee5a-0253-42be-98b8-e5cbc8da25b9.png"><img width="279" alt="image" src="https://user-images.githubusercontent.com/99929453/208487386-28613d55-9e27-4fb3-8af4-724a2cd9f6f0.png">



## Display
It will display a starting interface which the use has to press "Space" to start the game

<img width="476" alt="image" src="https://user-images.githubusercontent.com/99929453/208486925-66d63f2d-5a8c-44e2-a486-0487ba90ba56.png">
It will be randomly chosen for the AI or the player to go first

<img width="323" alt="image" src="https://user-images.githubusercontent.com/99929453/208486976-29401c86-ed59-4e39-96a6-8e34a7820788.png">
The AI will ask the user if he/she wants to play again (Press "Y"/"N" to answer)

<img width="591" alt="image" src="https://user-images.githubusercontent.com/99929453/208487014-77841095-4efc-494a-9088-cc95aaddd0f8.png">

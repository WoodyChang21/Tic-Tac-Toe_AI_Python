#---------------LOGIC------------------#
#Check for CPU win move
#Check for player win move
#Check for CPU fork opportunity
#Check for plyaer fork opportunity, but choose to force a block if there are two potential forks
#Check center
#Check Corners
#Check Sides

#Display board
def display_board(choice_list):
    row9 = "   |   |   "
    row8 = f" {choice_list[7]} | {choice_list[8]} | {choice_list[9]} "
    row7 = "   |   |   "
    row6 = "   |   |   "
    row5 = f" {choice_list[4]} | {choice_list[5]} | {choice_list[6]} "
    row4 = "   |   |   "
    row3 = "   |   |   "
    row2 = f" {choice_list[1]} | {choice_list[2]} | {choice_list[3]} "
    row1 = "   |   |   "
    separate_line = "-----------"
    print(row9)
    print(row8)
    print(row7)
    print(separate_line)
    print(row6)
    print(row5)
    print(row4)
    print(separate_line)
    print(row3)
    print(row2)
    print(row1)

#player pick what marker they want
def marker():
    choice = "Wrong"
    while choice not in ["X","O"]:
        choice = input("Player: Please enter your choice (X,O): ").upper()
    if choice == "X":
        return ("X","O")
    else:
        return ("O","X")

#Pick who's turn randomly
def random_turn():
    from random import randint
    if randint(1,2) == 1:
        print (f"Player goes first")
        return "Player"
    else:
        print ("AI goes first")
        return "AI"

#draws the marker on the position player pick
def player_pick_position(choice_list,marker):
    position = "11"
    while (int(position) not in range(1,10)) or choice_list[int(position)]=="X" or choice_list[int(position)]=="O":
        position = input("Pick your position (1-9): ")
        if int(position) not in range(1,10):
            print("Please enter valid position (1-9)")
            continue
        if choice_list[int(position)]=="X" or choice_list[int(position)]=="O":
            print("This position is occupied")
            
    choice_list[int(position)] = marker

#draws the marker on the position AI pick
def AI_pick_position(choice_list,marker,position):
    choice_list[position] = marker

#logic of detecting winning
def detect_win(choice_list):
    return (
    choice_list[1]==choice_list[2]==choice_list[3] or 
    choice_list[4]==choice_list[5]==choice_list[6] or 
    choice_list[7]==choice_list[8]==choice_list[9] or 
    choice_list[1]==choice_list[5]==choice_list[9] or
    choice_list[3]==choice_list[5]==choice_list[7] or 
    choice_list[1]==choice_list[4]==choice_list[7] or
    choice_list[2]==choice_list[5]==choice_list[8] or
    choice_list[3]==choice_list[6]==choice_list[9])

#if board is full
def check_full_board(choice_list):
    for index in range(1,10):
        if choice_list[index] not in ["X","O"]:
            return False
    return True

def empty_position(choice_list):
    #All the empty position
    index_list = []
    for index in range(1,10):
        if choice_list[index]!="X" and choice_list[index]!="O":
            index_list.append(index)
    return index_list

#Test if the position makes a FORK situation
def testForkMove(choice_list,mark,position):
    #Make a copy of the list
    copy_list = choice_list[:]

    #Mark the position
    copy_list[position] = mark
    new_copy_list = copy_list[:]

    #A list of empty position
    empty_list = empty_position(copy_list)

    #Count how many possible winning moves
    count = 0

    #Check all other empty positions
    for index in empty_list:
        copy_list[index]=mark
        if detect_win(copy_list):
            count+=1
            copy_list = new_copy_list[:]
        else:
            copy_list = new_copy_list[:]
    
    #return True if that position makes FORK situation
    return (count>=2)

#Return AI position
def AI_check(choice_list,AI_choice,player_choice):
    from random import randint
    import random

    #The list that will be tested throughout the function
    copy_list = choice_list[:]

    #All the empty position
    empty_list = empty_position(choice_list)

    #AI can win, return the position
    for position in empty_list:
        copy_list[position] = AI_choice
        if detect_win(copy_list):
            return position
        else:
            #Make sure the copy_list is setback to original list
            copy_list = choice_list[:]

    #Player can win, return the position
    for position in empty_list:
        copy_list[position] = player_choice
        if detect_win(copy_list):
            return position
        else:
            copy_list = choice_list[:]

    #Check if AI can make FORK situation
    for position in empty_list:
        if (testForkMove(copy_list,AI_choice,position)==True):
            return position
    
    #Check if player can make FORK situation, 
    # if two then block, but check don't make the player to form a fork again
    player_fork_count = 0
    FORK_position = []
    for position in empty_list:
        if testForkMove(copy_list,player_choice,position)==True:
            player_fork_count+=1
            FORK_position.append(position)

    #Prevent player to form the FORK
    if player_fork_count == 1:
        return FORK_position[0]
    
    #The player has more than one position to form the FORK
    #Make the player to block, but not on the FORK position
    elif player_fork_count>=2:
        for index in empty_list:
            copy_list[index]=AI_choice
            #The list with AI marked the trial position
            new_copy_list = copy_list[:]
            #The empty list after the AI marked the trial position
            new_empty_list = empty_position(copy_list)
            for position in new_empty_list:
                copy_list[position]=AI_choice
                if detect_win(copy_list) and position not in FORK_position:
                    return index
                else:
                    copy_list = new_copy_list[:]
            copy_list = choice_list[:]
    
    #if player has no winning potential, no fork potential
   
    #Play Center
    if choice_list[5]!="X" and choice_list[5]!="O":
        return 5
    #Play Corner
    Corner = [1,3,7,9]
    for i in random.sample(Corner,4):
        if (choice_list[i]!="X" and choice_list[i]!="O"):
            return i
    #Play Side
    Side = [2,4,6,8]
    for i in random.sample(Side,4):
        if (choice_list[i]!="X" and choice_list[i]!="O"):
            return i


#Ask for another game
def gameon():
    gameon = "default"
    while gameon!='Y' and gameon!='N':
        gameon = input("Do you want to play again (Y/N): ").upper()
        if gameon == "Y":
            return True
        if gameon == "N":
            return False
        else:
            print("Please enter Y or N")

#game logic
while True:
    choice_list = ["#","1","2","3","4","5","6","7","8","9"]
    display_board(choice_list)
    #Pick the marker
    (player_choice,AI_choice) = marker()
    turn = random_turn()
    while True:
        if turn == "Player":
            player_pick_position(choice_list,player_choice)
            display_board(choice_list)
            if detect_win(choice_list):
                print("Congratulation! You win!")
                break
                
            elif check_full_board(choice_list):
                print("It's a tie")
                break
                
            else:
                turn = "AI"
        else:
            AI_position = AI_check(choice_list,AI_choice,player_choice) #return position
            AI_pick_position(choice_list,AI_choice,AI_position)
            print(f"AI Position: {AI_position}")
            display_board(choice_list)
            if detect_win(choice_list):
                print("You Suck, AI win")
                break
                
            elif check_full_board(choice_list):
                print("It's a tie")
                break
                
            else:
                turn = "Player"
    if gameon()==False:
        break

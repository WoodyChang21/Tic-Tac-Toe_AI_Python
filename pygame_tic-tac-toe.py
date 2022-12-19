#---------------LOGIC------------------#
#Check for CPU win move
#Check for player win move
#Check for CPU fork opportunity
#Check for plyaer fork opportunity, but choose to force a block if there are two potential forks
#Check center
#Check Corners
#Check Sides

#Display board
import pygame
import time
import random
pygame.init()

#Tic-tac-toe board
board = pygame.image.load("white_board.png")

#Screen setup


#Basic color setup
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (61, 143, 186)

#Font setup
font_path = "C:/Users/User/Desktop/Python Project/font/joystix monospace.ttf"
start_font = pygame.font.Font(font_path,25, bold=True)

#Board coordinate
bottom_left = (247,403) #1
bottom = (374,401) #2
bottom_right = (502,403) #3
left = (248,275) #4
center = (373,277) #5
right = (496,275) #6
top_left = (254,149) #7
top_center = (374,151) #8
top_right = (497,152) #9

horizontal_left = range(214,294)
horizontal_center = range(334,414)
horizontal_right = range(446,547)
vertical_up = range(109,190)
vertical_center = range(239,319)
vertical_right = range(363,445) 

#Info for drawing x
x_coordinate = ['#']
#bottom_left
x_coordinate.append([[(216,377),(272,439)],[(216,439),(272,377)]])
#bottom_center
x_coordinate.append([[(344,377),(400,439)],[(344,439),(400,377)]])
#bottom_right
x_coordinate.append([[(463,377),(519,439)],[(463,439),(519,377)]])
#left
x_coordinate.append([[(216,243),(272,305)],[(216,305),(272,243)]])
#center
x_coordinate.append([[(344,243),(400,305)],[(344,305),(400,243)]])
#right
x_coordinate.append([[(462,243),(519,305)],[(462,305),(519,243)]])
#top_left
x_coordinate.append([[(216,124),(272,190)],[(216,190),(272,124)]])
#top_center
x_coordinate.append([[(344,124),(400,190)],[(344,190),(400,124)]])
#top_right
x_coordinate.append([[(462,124),(519,190)],[(462,190),(519,124)]])

def intro():
    run = False
    mesg = start_font.render("Welcome to", True, black)
    dis.blit(mesg,[dis_width/3+10,200])
    mesg_two = start_font.render("Undefeatable Tic-tac-toe AI", True, black)
    dis.blit(mesg_two,[dis_width/6-20,240])
    mesg_three = start_font.render("Press Space to start", True, black)
    dis.blit(mesg_three,[dis_width/3-70,280])
    pygame.display.update()
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dis.fill(white)
                    run = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break

def AI_win_string():
    mesg = start_font.render("AI wins!!!", True, black)
    dis.blit(mesg,[282,539])
    pygame.display.update()

def player_win_string():
    mesg = start_font.render("Player wins!!!", True, black)
    dis.blit(mesg,[282,539])
    pygame.display.update()

def tie_string():
    mesg = start_font.render("It's a tie",True,black)
    dis.blit(mesg,[282,539])
    pygame.display.update()

def ask_for_another_round():
    asking = True
    dis.fill(white)
    mesg = start_font.render("Do you want to challenge again? (Y/N)", True, black)
    dis.blit(mesg,[25,240])
    pygame.display.update()
    while asking:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    asking = False
                    return True
                if event.key == pygame.K_n:
                    asking = False
                    return False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def turn_string(turn):
    msg = f"{turn} goes first!"
    mesg = start_font.render(msg,True,black)
    dis.blit(mesg,[dis_width/4+10,200])
    pygame.display.update()

def random_turn():
    from random import randint
    if randint(1,2) == 1:
        return "Player"
    else:
        return "AI"

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
        if choice_list[index] not in ["x","o"]:
            return False
    return True

#Player's input
#choice_list = ["#","1","2","3","4","5","6","7","8","9",]
def player_draw_position(choice_list):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            #Top left
            if position[0] in horizontal_left and position[1] in vertical_up:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #top_center
            elif position[0] in horizontal_center and position[1] in vertical_up:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #top_right
            elif position[0] in horizontal_right and position[1] in vertical_up:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #left
            elif position[0] in horizontal_left and position[1] in vertical_center:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #center
            elif position[0] in horizontal_center and position[1] in vertical_center:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #right
            elif position[0] in horizontal_right and position[1] in vertical_center:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #bottom_left
            elif position[0] in horizontal_left and position[1] in vertical_right:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #bottom
            elif position[0] in horizontal_center and position[1] in vertical_right:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            #bottom_right
            elif position[0] in horizontal_right and position[1] in vertical_right:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            #Top left
            if position[0] in horizontal_left and position[1] in vertical_up and choice_list[7]!="x" and choice_list[7]!="o":
                pygame.draw.circle(dis,black,top_left,40,width=10)
                choice_list[7] = "o"
            #top_center
            elif position[0] in horizontal_center and position[1] in vertical_up and choice_list[8]!="x" and choice_list[8]!="o":
                pygame.draw.circle(dis,black,top_center,40,width=10)
                choice_list[8] = "o"
            #top_right
            elif position[0] in horizontal_right and position[1] in vertical_up and choice_list[9]!="x" and choice_list[9]!="o":
                pygame.draw.circle(dis,black,top_right,40,width=10)
                choice_list[9] = "o"
            #left
            elif position[0] in horizontal_left and position[1] in vertical_center and choice_list[4]!="x" and choice_list[4]!="o":
                pygame.draw.circle(dis,black,left,40,width=10)
                choice_list[4] = "o"
            #center
            elif position[0] in horizontal_center and position[1] in vertical_center and choice_list[5]!="x" and choice_list[5]!="o":
                pygame.draw.circle(dis,black,center,40,width=10)
                choice_list[5] = "o"
            #right
            elif position[0] in horizontal_right and position[1] in vertical_center and choice_list[6]!="x" and choice_list[6]!="o":
                pygame.draw.circle(dis,black,right,40,width=10)
                choice_list[6] = "o"
            #bottom_left
            elif position[0] in horizontal_left and position[1] in vertical_right and choice_list[1]!="x" and choice_list[1]!="o":
                pygame.draw.circle(dis,black,bottom_left,40,width=10)
               
                choice_list[1] = "o"
            #bottom
            elif position[0] in horizontal_center and position[1] in vertical_right and choice_list[2]!="x" and choice_list[2]!="o":
                pygame.draw.circle(dis,black,bottom,40,width=10)
                choice_list[2] = "o"
            #bottom_right
            elif position[0] in horizontal_right and position[1] in vertical_right and choice_list[3]!="x" and choice_list[3]!="o":
                pygame.draw.circle(dis,black,bottom_right,40,width=10)
                choice_list[3] = "o"
            pygame.display.update()
    return choice_list

#This mark the position
def AI_pick_position(choice_list,position):
    choice_list[position] = "x"

def AI_draw_position(position):
    if position == 1:
        pygame.draw.line(dis,black,x_coordinate[1][0][0],x_coordinate[1][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[1][1][0],x_coordinate[1][1][1],width=15)
    if position == 2:
        pygame.draw.line(dis,black,x_coordinate[2][0][0],x_coordinate[2][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[2][1][0],x_coordinate[2][1][1],width=15)
    if position == 3:
        pygame.draw.line(dis,black,x_coordinate[3][0][0],x_coordinate[3][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[3][1][0],x_coordinate[3][1][1],width=15)
    if position == 4:
        pygame.draw.line(dis,black,x_coordinate[4][0][0],x_coordinate[4][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[4][1][0],x_coordinate[4][1][1],width=15)
    if position == 5:
        pygame.draw.line(dis,black,x_coordinate[5][0][0],x_coordinate[5][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[5][1][0],x_coordinate[5][1][1],width=15)
    if position == 6:
        pygame.draw.line(dis,black,x_coordinate[6][0][0],x_coordinate[6][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[6][1][0],x_coordinate[6][1][1],width=15)
    if position == 7:
        pygame.draw.line(dis,black,x_coordinate[7][0][0],x_coordinate[7][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[7][1][0],x_coordinate[7][1][1],width=15)
    if position == 8:
        pygame.draw.line(dis,black,x_coordinate[8][0][0],x_coordinate[8][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[8][1][0],x_coordinate[8][1][1],width=15)
    if position == 9:
        pygame.draw.line(dis,black,x_coordinate[9][0][0],x_coordinate[9][0][1],width=15)
        pygame.draw.line(dis,black,x_coordinate[9][1][0],x_coordinate[9][1][1],width=15)
    pygame.display.update()    
    


def empty_position(choice_list):
    #All the empty position
    index_list = []
    for index in range(1,10):
        if choice_list[index]!="x" and choice_list[index]!="o":
            index_list.append(index)
    return index_list

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

    AI_choice = "x"
    player_choice = "o"

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
    if choice_list[5]!="x" and choice_list[5]!="o":
        return 5
    #Play Corner
    Corner = [1,3,7,9]
    for i in random.sample(Corner,4):
        if (choice_list[i]!="x" and choice_list[i]!="o"):
            return i
    #Play Side
    Side = [2,4,6,8]
    for i in random.sample(Side,4):
        if (choice_list[i]!="x" and choice_list[i]!="o"):
            return i


#default choice_list

if(__name__=="__main__"):
    gameon = True
    while gameon:
        #Game setup
        gameon = True
        #Default choice list
        choice_list = ["#","1","2","3","4","5","6","7","8","9"]
        #Screen setup
        dis_width = 800
        dis_height = 600
        dis = pygame.display.set_mode((dis_width,dis_height))
        dis.fill(white)

        #Intro page
        intro()
        #Turn page
        turn = random_turn()
        turn_string(turn)
        time.sleep(1)
        #Board
        dis.fill(white)
        dis.blit(board,(200,100))
        pygame.display.update()
        while True:
            previous_choice_list = choice_list[:]
            #it only runs when the player input a valid position
            if turn == "Player":
                if previous_choice_list != player_draw_position(choice_list):
                    if detect_win(choice_list):
                        player_win_string()
                        time.sleep(1)
                        gameon = ask_for_another_round()
                        break
                    elif check_full_board(choice_list):
                        tie_string()
                        time.sleep(1)
                        gameon = ask_for_another_round()
                        break
                    turn = "AI"
                    time.sleep(0.5)
            if turn == "AI":
                AI_position = AI_check(choice_list,"x","o")
                AI_pick_position(choice_list,AI_position)
                AI_draw_position(AI_position)
                if detect_win(choice_list):
                    AI_win_string()
                    time.sleep(1)
                    gameon = ask_for_another_round()
                    break
                elif check_full_board(choice_list):
                    tie_string()
                    time.sleep(1)
                    gameon = ask_for_another_round()
                    break
                turn = "Player"
                time.sleep(0.5)
    else:
        pass
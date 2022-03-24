# Name: Shahd Khaled
#ID: 20210182

# Tic-Tac-Toe with numbers. A board of 3 x 3 is displayed and player 1 takes odd numbers 1,
# 3, 5, 7, 9 and player 2 takes even numbers 0, 2, 4, 6, 8. Players take turns to write their
# numbers. Odd numbers start. Use each number only once. The first person to complete a line
# that adds up to 15 is the winner. The line can have both odd and even numbers.

board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
board2 = []

# function that print the board


def printboard():
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print(f" {board[7]} | {board[8]} | {board[9]}")

    # function that print the player who will play


def player_turn(x):
    if x % 2 == 1:
        print("player 1 Turn")
    if x % 2 == 0:
        print("player 2 Turn")


x = 1
# discribe the game
print("Tic-Tac-Toe with numbers. A board of 3 x 3 is displayed and player 1 takes odd numbers 1,\
    3, 5, 7, 9 and player 2 takes even numbers 0, 2, 4, 6, 8. Players take turns to write their\
    numbers. Odd numbers start. Use each number only once. The first person to complete a line\
    that adds up to 15 is the winner. The line can have both odd and even numbers.")
print("The places of the board:\n")
print(f" 1 | 2 | 3")
print(f" 4 | 5 | 6")
print(f" 7 | 8 | 9\n\n")

try:
    while True:
        printboard()
        print(board2)
        player_turn(x)
    # determine the player
        if x % 2 == 1:
            player_inp1 = int(input("player 1 enter an odd number: "))
    # check if the the number is repeated
            if player_inp1 in board2:
                print("The number has been chosen")
            else:
                if player_inp1 > 0:
                    if player_inp1 % 2 == 1:
                        the_place = int(input("Enter the place: "))
                        board2.append(player_inp1)
                        board[the_place] = player_inp1
                        x += 1
    # check winning
                        if board[1]+board[2]+board[3] == 15 or board[4] + board[5] + board[6] == 15 or board[7] + board[8] + board[9] == 15:
                            print("player 1 won")
                            printboard()
                            break
                        if board[1]+board[4]+board[7] == 15 or board[2] + board[5] + board[8] == 15 or board[3] + board[6] + board[9] == 15:
                            print("player 1 won")
                            printboard()
                            break
                        if board[1]+board[5]+board[9] == 15 or board[3] + board[5] + board[7] == 15:
                            print("player 1 won")
                            printboard()
                            break
                    else:
                        print("False input enter an odd number")
                else:
                    print("negative error")
                printboard()
                print(board2)
                player_turn(x)
    # determine the player
        if x % 2 == 0:
            player_inp2 = int(input("player 2 enter an even number: "))
    # check if the the number is repeated
            if player_inp2 in board2:
                print("The number has been chosen")
            else:
                if player_inp2 > 0:
                    if player_inp2 % 2 == 0:
                        the_place2 = int(input("Enter the place: "))
                        board2.append(player_inp2)
                        board[the_place2] = player_inp2
                        x += 1
    # check winning
                        if board[1]+board[2]+board[3] == 15 or board[4] + board[5] + board[6] == 15 or board[7] + board[8] + board[9] == 15:
                            print("player 2 won")
                            printboard()
                            break
                        if board[1]+board[4]+board[7] == 15 or board[2] + board[5] + board[8] == 15 or board[3] + board[6] + board[9] == 15:
                            print("player 2 won")
                            printboard()
                            break
                        if board[1]+board[5]+board[9] == 15 or board[3] + board[5] + board[7] == 15:
                            print("player 2 won")
                            printboard()
                            break
                    else:
                        print("False input enter an even number")
                else:
                    print("negative error")


except:
    print("Invaild input")

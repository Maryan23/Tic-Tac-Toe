#!/usr/bin/env python3.8

from player import Player

user=Player()
input_list=[" ", " ", " ", " ", " ", " ", " ", " ", " "]

def show_grid():
    """Draws the board"""
    print("\n")
    print(f'  {input_list[0]}  |  {input_list[1]}  |  {input_list[2]}  ')
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(f'  {input_list[3]}  |  {input_list[4]}  |  {input_list[5]}  ')
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(f'  {input_list[6]}  |  {input_list[7]}  |  {input_list[8]}  ')

def win_state():
    """Defines all possible winning arrangement"""
    if input_list[0]==input_list[1] and input_list[1]==input_list[2]:
        if input_list[0] != " ":
            return True

    elif input_list[3]==input_list[4] and input_list[4]==input_list[5]:
        if input_list[3] != " ":
            return True

    elif input_list[6]==input_list[7] and input_list[7]==input_list[8]:
        if input_list[6] != " ":
            return True

    elif input_list[0]==input_list[3] and input_list[3]==input_list[6]:
        if input_list[0] != " ":
            return True

    elif input_list[1]==input_list[4] and input_list[4]==input_list[7]:
        if input_list[1] != " ":
            return True

    elif input_list[2]==input_list[5] and input_list[5]==input_list[8]:
        if input_list[2] != " ":
            return True

    elif input_list[0]==input_list[4] and input_list[4]==input_list[8]:
        if input_list[0] != " ":
            return True

    elif input_list[2]==input_list[4] and input_list[4]==input_list[6]:
        if input_list[2] != " ":
            return True

    else:
        return False

def main():
    print("I see you are here to play :) .")
    player1 = input("Player 1 Enter your name.")
    player2 = input("Player 2 Enter your name.")
  
    which_player=True 
    
    is_stalemate= True 
    
        
    print("     TIC-TAC_TOE")
    print("This is how the board looks like\n")
    
    print(" 1   | 2   | 3   ")
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(" 4   | 5   | 6   ")
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(" 7   | 8   | 9   ")   
    print("\n")

    print("Let the game begin!")
    while len(user.moves_available)>0:
        value_error=False
        
        if which_player==True:
            print(f"\n{player1}:")
            print("Available moves:")
            user.show_available_moves()
            show_grid() #prints the board
            print(f"{player1} make a move")
            
            try:
                slot=int(input()) #Accepts input of type integer
            except ValueError:
                value_error=True
                print("Kindly use numbers 1-9!!") #What is to be shown when input is not an integer!
            
            if value_error==False:
                if user.validate_move(slot):
                    input_list[slot-1]="X"
                    user.move_made(slot)
                    which_player=False
                    
                    if win_state():
                        show_grid()

                        print(f"\n----- {player1} WINS! -----\n               END")                    
                        
                        is_stalemate=False
                        break
                else:
                    print("******Invalid move, try again******")
                    which_player=True   

        else:
            print(f"\n{player2}:")
            print("Available moves:")
            user.show_available_moves()
            show_grid()
            print(f"{player2} make a move.")
            try:
                slot=int(input())
            except ValueError:
                value_error=True
                print("Kindly use numbers 1-9!!")
            
            if value_error==False:
                if user.validate_move(slot):
                    input_list[slot-1]="O"
                    user.move_made(slot)
                    which_player=True

                    if win_state():
                        show_grid()
                        print(f"\n-----{player2} WINS! -----")                    
                        print("              END")
                        is_stalemate=False
                        break
                else:
                    print("Invalid Move! Repeat.")
                    which_player=False

    if is_stalemate:
        show_grid()
        print("\nThe game has ended in a draw\n      END")
    

if __name__ == "__main__":
    main ()
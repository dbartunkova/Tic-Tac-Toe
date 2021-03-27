separator = (42 * "=")
separator2 = (42 * "-")
Welcome = "Welcome to Tic Tac Toe"
Rules = "GAME RULES:"

print(Welcome)
print(separator)
print(Rules.center(40))

print("""
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
""")

print(separator)
print("Let's start the game")
print(separator2)

The_Board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in The_Board:
    board_keys.append(key)


def print_Board(board):
    print("\n")
    print(" +---+---+---+")
    print(" | " + board['1'] + " | " + board['2'] + " | " + board['3'] + " | ")
    print(" +---+---+---+")
    print(" | " + board['4'] + " | " + board['5'] + " | " + board['6'] + " | ")
    print(" +---+---+---+")
    print(" | " + board['7'] + " | " + board['8'] + " | " + board['9'] + " | ")
    print(" +---+---+---+")
    print("\n")


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_Board(The_Board)
        print(separator)
        
        move = input(f"Player {turn} | Please enter your move number: ")

        print(separator)

        if The_Board[move] == ' ':
            The_Board[move] = turn
            count += 1
        else:
            print(f"This place is already filled.\nPlease enter your move number again:")
            continue

        
        if count >= 5:
            if The_Board['1'] == The_Board['2'] == The_Board['3'] != ' ':
                print_Board(The_Board)               
                print(f"Congratulations, the player {turn} WON!")                 
                break
            elif The_Board['4'] == The_Board['5'] == The_Board['6'] != ' ': 
                print_Board(The_Board)               
                print(f"Congratulations, the player {turn} WON!")  
                break
            elif The_Board['7'] == The_Board['8'] == The_Board['9'] != ' ': 
                print_Board(The_Board)              
                print(f"Congratulations, the player {turn} WON!")  
                break
            elif The_Board['1'] == The_Board['4'] == The_Board['7'] != ' ': 
                print_Board(The_Board)              
                print(f"Congratulations, the player {turn} WON!")  
                break
            elif The_Board['2'] == The_Board['5'] == The_Board['8'] != ' ': 
                print_Board(The_Board)               
                print(f"Congratulations, the player {turn} WON!")   
                break
            elif The_Board['3'] == The_Board['6'] == The_Board['9'] != ' ': 
                print_Board(The_Board)               
                print(f"Congratulations, the player {turn} WON!")  
                break 
            elif The_Board['7'] == The_Board['5'] == The_Board['3'] != ' ':
                print_Board(The_Board)               
                print(f"Congratulations, the player {turn} WON!")    
                break
            elif The_Board['1'] == The_Board['5'] == The_Board['9'] != ' ': 
                print_Board(The_Board)              
                print(f"Congratulations, the player {turn} WON!")    
                break 

        
        if count == 9:        
            print(f"It's a Tie!")

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    

if __name__ == "__main__":
    game()
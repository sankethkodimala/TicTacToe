import random
import copy

class TicTacToe:
    def __init__(self,player,opp): #Constructor, initializes empty board, the character user wants to be, and the opponent.
        self.board =[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = player
        self.opp = opp.lower()

    def user_move(self): # Function for setting user's move on the board.
        while True: # Loop to ensure that inputs are valid
            try:
                row,col = (input("Move?(in 'row col' format): ")).split() # getting desired row and column for the move

                row = int(row)
                col = int(col)

            except ValueError: # Checking if both row and col are integers
                print("Both inputs are not integers. Make sure rows and cols are between 0-2. Try again")
                print()
                continue

            if row > 2 or col > 2: # Checking if inputs are in bounds
                print("Out of bounds, try again! Rows and Cols are 0-2")
                print()
                continue

            if self.board[row][col] != " ": # Checking if desired spot is empty on the board
                print("Spot already filled. Pick a different spot")
                print()
            
            else:
                break
       
        self.board[int(row)][int(col)] = self.player # Setting user's move on the board

    def game_over(self,board): # Function to check the status of the game
        result = "Not Over"
        
        for row in range(3): #checking each row for 3 in a row
            count = 0
            for col in range(3):
                if board[row][col] == self.player:
                    count += 1
            
            if count == 3: #if three in a row, returns win
                return "Win"


        for col in range(3): #checking each column for 3 in a row
            count = 0
            for row in range(3):
                if board[row][col] == self.player:
                    count += 1
        
            if count  == 3: #if three in a row, returns win
                return "Win"


        for i in range(3): # checking the diagonal(upper left to bottom right) for three in a row
            result = "Win"
            if board[i][i] != self.player:
                result = "Not Over"
                break

        if result == "Win":
            return result #if three in a row, returns win

        for i in range(3): # checking the opposite diagonal(top right to bottom left) for three in a row
            result = "Win"
            if board[i][2-i] != self.player:
                result = "Not Over"
                break

        if result == "Win": #if three in a row, returns win
            return result


        count = 0 # checking if every spot is filled up
        for i in range(3):
            for j in range(3):
                if board[i][j] != " ":
                    count +=1


        if result == "Not Over" and count == 9: # If no one won and all spots taken, it is a draw
            result = "Draw"
            return result
    
        return result

    def next_player(self): # Function that changes to next player's character
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'


    def print_board(self): # Function to print the board
        for i in range(3):
            print(self.board[i])

    def game(self): # Function for the full game

        while(self.game_over(self.board) == "Not Over"): # While the game is not over
            print("It is", self.player, "'s turn!")
            self.print_board()
            self.user_move() # user's turn, calls user_move function
           
            if self.game_over(self.board) != "Not Over": # if draw or win after user's turn, break
                break
             # next player's turn
           
            if self.opp == "medium": # if selected opponent is medium_borg
                self.next_player() # next player's turn
                self.med_borg() # call medium borg function to make a move
                if self.game_over(self.board) != "Not Over": # checking if draw or win occurs after turn
                    break
           
            if self.opp == "easy": # if selected opponent is easy bord
                self.next_player() # next player's turn
                self.easy_borg() # call easy borg function to make a move
                if self.game_over(self.board) != "Not Over": # checking if draw or win occurs after turn
                    break
            
            self.next_player() # Goes back to user's turn if opponent is bot, otherwise goes to user 2's turn.
            

        # Checking if game ended it a draw or win and priting final board
        if self.game_over(self.board) == "Draw":
            print("It's a draw!")
            self.print_board()
        else:
            print("Game over!",self.player, "Wins!!")
            self.print_board()

    def easy_borg(self): # function for easy borg
        row = random.randint(0,2) # get's random row and col values to make a move
        col = random.randint(0,2)
        if self.board[row][col] == " ": # If random spot is empty, sets is character at that spot
            self.board[row][col] = self.player
        else: # Otherwiser, it recursively calls the function again for a different random spot
            self.easy_borg() 



    def med_borg(self): # Function for medium borg
        move = False
        original_char = self.player

        for row in range(3): # checking if there is a spot where it can win
            for col in range(3):
                bcopy = copy.deepcopy(self.board) # makes a deepcopy of the board and tries every empty spot
                if bcopy[row][col] == " ":
                    bcopy[row][col] = self.player
                    if self.game_over(bcopy) == "Win": # If one of those spots results in a win, then it places its character there
                        self.board[row][col] = self.player
                        move = True
                        break
            if move:
                break
    

        if not move: # If it has found no spots to win, it checks to see if there is a spot where it can lose
            self.next_player() # Switches characters to check from user's persepctive 
            for row in range(3): 
                for col in range(3):
                    bcopy = copy.deepcopy(self.board) # makes deepcopy of the board and tries every empty spot as the user's character
                    if bcopy[row][col] == " ":
                        bcopy[row][col] = self.player
                        if self.game_over(bcopy) == "Win": # If there is a place where the user can win, the bot places its character there to prevent the win
                            self.next_player()
                            self.board[row][col] = self.player
                            move = True
                            break
                if move:
                    break
       
        self.player = original_char 
        if not move: # If there are no spots where it can win or lose, it places its character in a random spot(same as easy borg)
            self.easy_borg()


    # def hard_bot(self,board, depth):
        
# Setting up game for user to play
while True: # Ensuring the user selects one of the given modes
    mode = input("Who do you want to play against?(Person, Easy, or Medium) ").lower()
    if mode in ["person", "easy", "medium"]:
        break
    else:
        print("Invalid choice. Please enter Person, Easy, or Medium.")
            
while True:
    character = input("Select your charater. X or 0 ").upper()
    if character in ["X", "O"]:
        break
    else:
        print("Invalid Choice. Choose X or O")
game = TicTacToe(character, mode) # creating TickTacToe object with user's inputs
game.game() # starting the game

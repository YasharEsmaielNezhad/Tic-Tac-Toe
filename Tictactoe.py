class Tictactoe:
    def __init__(self) -> None:
        self.board = ["-" , "-" , "-",
                "-" , "-" , "-",
                "-" , "-" , "-"]
    def board(Board):
        print (Board[1] + " | " +Board[2] + " | " +Board[3] + " | " )
        print("-------------------")
        print (Board[4] + " | " +Board[5] + " | " +Board[6] + " | " )
        print("-------------------")
        print (Board[7] + " | " +Board[8] + " | " +Board[9] + " | " )


c=Tictactoe()

def computer(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] == "O"
            switchPlayer()
computer(board)
    checkWin()
    checkTie(board)
import numpy as np 

possible_moves = [1,2,3,4,5,6,7,8,9]
table = {"top-L" : "" , "top-M" : "" , "top-R" : "" ,
        "mid-L" : " " , "mid-M" : " ", "mid-R" : " ",
        "low-L" : " " , "low-M" : " " , "low-R" : " "}

def print_table():
    print(table["top-L"] + " | " + table["top-M"] + " | " + table["top-R"])
    print("--------------")
    print(table["mid-L"] + " | " + table["mid-M"] + " | " + table["mid-R"])
    print("--------------")
    print(table["low-L"] + " | " + table["low-M"] + " | " + table["low-R"])


def move_user():
    if possible_moves == []:
        print("END")
    move = int(input(f"move: {possible_moves}: "))

    if move == 1:
        possible_moves.remove(move)
        table["top-L"] = "x"
    elif(move == 2):
        possible_moves.remove(move)
        table["top-M"] = "x"
    elif(move == 3):
        possible_moves.remove(move)
        table["top-R"] = "x"
    elif(move == 4):
        possible_moves.remove(move)
        table["mid-L"] = "x"
    elif(move == 5):
        possible_moves.remove(move)
        table["mid-M"] = "x"
    elif(move == 6):
        possible_moves.remove(move)
        table["mid-R"] = "x"
    elif(move == 7):
        possible_moves.remove(move)
        table["low-L"] = "x"
    elif(move == 8):
        possible_moves.remove(move)
        table["low-M"] = "x"
    elif(move == 9):
        possible_moves.remove(move)
        table["low-R"] = "x"

def move_computer():
    if possible_moves == []:
        print("END")
    move = np.random.choice(possible_moves)

    if move == 1:
        possible_moves.remove(move)
        table["top-L"] = "o"
    elif(move == 2):
        possible_moves.remove(move)
        table["top-M"] = "o"
    elif(move == 3):
        possible_moves.remove(move)
        table["top-R"] = "o"
    elif(move == 4):
        possible_moves.remove(move)
        table["mid-L"] = "o"
    elif(move == 5):
        possible_moves.remove(move)
        table["mid-M"] = "o"
    elif(move == 6):
        possible_moves.remove(move)
        table["mid-R"] = "o"
    elif(move == 7):
        possible_moves.remove(move)
        table["low-L"] = "o"
    elif(move == 8):
        possible_moves.remove(move)
        table["low-M"] = "o"
    elif(move == 9):
        possible_moves.remove(move)
        table["low-R"] = "o"


def main():
    while True:
        out = move_user()
        if out == "END":
            print("GAME IS ENDED")
            break
        print_table()

        c_out = move_computer()
        if c_out == "END":
            print("GAME IS ENDED")
            break
        print_table()


main()
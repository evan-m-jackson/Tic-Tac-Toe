spaces = [" "] * 9
GAME_ON = True
TURN = 1


def create_board(spaces):
    board = ""
    for i in range(0, len(spaces)):
        if i % 3 == 0:
            board += f" {spaces[i]} "
        else:
            board += f"| {spaces[i]} "
        if i == 2 or i == 5:
            board += "\n-----------\n"

    print(board)


def game_over(spaces):
    create_board(spaces)
    print("GAME OVER")


def player_choice():
    choice = None
    while choice is None:
        try:
            num = int(input("Please select your space (enter 1-9): "))
            if num < 1 or num > 9:
                print("Please enter a number between 1 and 9")
            else:
                choice = num
        except:
            print("Please enter a whole number between 1 and 9")
    return choice - 1


def mark_board(spaces, choice, player):
    if spaces[choice] == " ":
        spaces[choice] = player
        return True
    else:
        return False


def check_for_win(s1, s2, s3):
    return s1 == s2 and s2 == s3 and s3 != " "


def check_win_combos(s):
    return (
        check_for_win(s[0], s[1], s[2])
        or check_for_win(s[3], s[4], s[5])
        or check_for_win(s[6], s[7], s[8])
        or check_for_win(s[0], s[3], s[6])
        or check_for_win(s[1], s[4], s[7])
        or check_for_win(s[2], s[5], s[8])
        or check_for_win(s[0], s[4], s[8])
        or check_for_win(s[2], s[4], s[6])
    )


def check_for_tie(spaces):
    return " " not in spaces


print(
    "WELCOME TO TIC TAC TOE!\n Please see the corresponding number for each space below:"
)
create_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

while GAME_ON:
    if TURN == 1:
        player = "X"
    else:
        player = "O"
    print(f"It is Player {player}'s turn!")
    create_board(spaces)
    choice = player_choice()

    # Check that space is available
    if mark_board(spaces, choice, player):

        if check_win_combos(spaces):
            game_over(spaces)
            print(f"Player {player} wins!")
            GAME_ON = False

        elif check_for_tie(spaces):
            game_over(spaces)
            print("Tie!")
            GAME_ON = False
        else:
            TURN *= -1

    else:
        print("That space is already taken.  Please choose another!")

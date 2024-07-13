import sys
def get_score(red, blue):
    # returns the score based remaining marbles
    if red == 0 and blue == 0:
        return 0
    elif red == 0:
        return 3 * blue
    elif blue == 0:
        return 2 * red
    else:
        return 2 * red + 3 * blue
def legal_moves(red, blue):
    # all possible moves for picking the pile
    if blue > 0 and red > 0:
        return ([red, blue-1], [red-1, blue])
    elif blue > 0:
        return ([red, blue-1])
    elif red > 0:
        return ([red-1, blue])
    else:
        return ()
def minplayer(red, blue, alpha_gain, beta_gain, depth):
    # minplayer turn
    points = get_score(red, blue)
    if red == 0 or blue == 0:
        return 1 * points, None
    if depth == 0:
        return get_score(red, blue), None  # get_score function
    val = float('+inf')
    color = None
    # all possible moves
    for choice in legal_moves(red, blue):
        _, choice2 = maxplayer(choice[0], choice[1], alpha_gain, beta_gain, depth - 1)
        val = min(val, get_score(choice[0], choice[1]))
        # alpha-beta check
        if val <= alpha_gain:
            return val, choice2
        beta_gain = min(beta_gain, val)
        color = choice2
    return val, color
def maxplayer(red, blue, alpha_gain, beta_gain, depth):
    #max player turn
    points = get_score(red, blue)
    if red == 0 or blue == 0:
        return -1 * points , None
    if depth == 0:
        return get_score(red, blue), None

    list_of_piles = legal_moves(red, blue)
    best_value = float('-inf')
    best_move = None
    for choice in list_of_piles:
        value = minplayer(choice[0], choice[1], alpha_gain, beta_gain, depth - 1)[0]
        # comparing the score  with  alpha beta values
        if value > best_value:
            best_value = value
            best_move = choice
        if best_value >= beta_gain:
            return best_value, best_move
        alpha_gain = max(alpha_gain, best_value)
    return best_value, best_move
def alphabetapruning(red, blue, depth):
    # min max algorithm with alpha and beta pruning
    val, effect = maxplayer(red, blue, float('-inf'), float('+inf'), depth)
    return (val, effect) if effect else (val, None)
def red_blue_nim(red, blue, player_turn="Computer", depth=0):
    player_turn = player_turn.lower()
    while not (red == 0 or blue == 0):
        if player_turn == "computer":
            # computer turn
            print(f"Current state: Red - {red}, Blue - {blue}")
            _, effect = alphabetapruning(red, blue, depth)
            if effect[0] == red - 1:
                print("Computer chose red pile to remove")
                red = red - 1
            elif effect[1] == blue - 1:
                print("Computer chose blue pile to remove")
                blue = blue - 1
            player_turn = "human"
        else:
            # human turn
            print(f"Current status: red - {red}, blue - {blue}")
            marble = input("Choose a pile (red or blue): ")
            while marble != 'red' and marble != 'blue':
                marble = input("Invalid input! Pick a pile (red or blue): ")
            if marble == 'red':
                red = red - 1
            else:
                blue = blue - 1
            player_turn = "computer"

    print(f"{player_turn} wins with {get_score(red, blue)} points")
if len(sys.argv) == 5:
    # reading inputs from command line arguments
    red = sys.argv[1]
    blue = sys.argv[2]
    player_turn = sys.argv[3]
    depth = sys.argv[4]
elif len(sys.argv) == 4:
    red = sys.argv[1]
    blue = sys.argv[2]
    player_turn = sys.argv[3]

if not red.isdigit():
    # if red is not a number then renter
    red = input("Please enter the Number of red marbles: ")
if not blue.isdigit():
    # if  blue is not a number renter
    blue = input("Please enter the Number of blue marbles: ")

if player_turn.isnumeric() and len(sys.argv) == 4:
    # defaulting to first player computer
    depth = player_turn
    player_turn = "computer"
    print("first player defaulted to computer")

red_blue_nim(int(red), int(blue), player_turn, int(depth))

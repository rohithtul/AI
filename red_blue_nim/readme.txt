Programming language: Python 3.10.6
code Structure:
below are all the methos from top to bottom.
 1. get_score() which evaluates the score and eval function.
 2. legal_moves() returns all possible moves.
 3. minplayer() returns the min-max algorithm min player
 4. maxplayer() returns the min-max algorithm max player
 5. alphabetapruning() which is used for computer turn uses maxplayer() function in it.
 6. red_blue_nim() this is game function which works based on human or computer turn and pick the pile 
    until one of the marble is empty and will reurn the score of winner.
 7.red_blue_nim() method is called for game processing and inputs are read from command line arguments.

compile and run instrunctions:
1. open the command prompt and go to the project folder where the python file is located.
2. run the command: <py/python3> red_blue_nim.py <num-red> <num-blue> <first-player> <depth>
3. Depth limited search is implemented in the program so must pass the <depth> value in the command prompt for successful run.

Note:
Make sure you pass atleast 3 parameters in the run command.
 



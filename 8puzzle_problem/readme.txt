
How code is structured:
1.I have used Python 3.10.6 for this program
2. Open the command prompt or terminal
3. cd <Project_Folder>
4.To run the code, run the below command in terminal
  py expense_8_puzzle.py start.txt goal.txt dfs true
5. Make sure start.txt, goal.txt are in the same Project_Folder
6.import datetime, deque, PriorityQueue,heapq,sys incase if you have issues with packages.

How code is structured:
python file name :expense_8_puzzle.py

8-puzzle problem solving methods:
I have used get_position() method for getting the 0th position in the list.
get_possible_actions() to give the list of actions for each move.
get_apply_actions to swap the tiles for each action.

Search methods for goal state finding:
1.Bfs,Dfs,Dls,Ids:-
   a)I have used dequeue for all these searches added the nodes to queue
     maintained the explored list to manage closed set.Applied the searches accordingly for each method.
   b) DLS: enter the depth limit for this search as a input.

2.Ucs- I have used Priority queue for popping the least cost
  Astar,Greedy- I have used Heap queue to heapfiy states in the order applied heuristic accordingly

  According to the method naming convention algorithm works.
  Defaults: Dump_flag is false, method = a*

Trace file Instructions:
1. If trace file is required use below commands, and trace file written in same directory.
trace file name: trace_yyyymmdd_hhmmss.txt
python3 expense_8_puzzle start_file goal_file.txt greedy true
python3 expense_8_puzzle start_file goal_file.txt bfs true
python3 expense_8_puzzle start_file goal_file.txt ids true
python3 expense_8_puzzle start_file goal_file.txt ucs true
python3 expense_8_puzzle start_file goal_file.txt dls true
python3 expense_8_puzzle start_file goal_file.txt dfs true
python3 expense_8_puzzle start_file goal_file.txt a* true
 Note: use py or python3 for above commands.

2. If trace file is not required run the below commands for each algorithm
python3 expense_8_puzzle start_file goal_file.txt a*
python3 expense_8_puzzle start_file goal_file.txt bfs
python3 expense_8_puzzle start_file goal_file.txt ids
Note : For dls, limit has to be given from user in the termmial after running the command
python3 expense_8_puzzle start_file goal_file.txt greedy
python3 expense_8_puzzle start_file goal_file.txt dls
python3 expense_8_puzzle start_file goal_file.txt ucs
python3 expense_8_puzzle start_file goal_file.txt dfs
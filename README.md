# Checkers



                                                ------GAME INTRODUCTION------

The board game Checkers has been played by humans for decades now. In this project we have attempted to design a bot which will function in such a way as to excel human intelligence. In order to do so, the most common approach was used to solving any adversarial problem; the minimax algorithm with alpha-beta pruning. This strategy has proven successful in attempts to outsmart the human mind.



	                                            ------GAME PROPERTIES------
                                                          
Our implementation relies on the rules of English draughts as they're described in Wikipedia, and on some additional rules that follow from them. Such as: 

1.  Regular capture is possible only in forward direction, except if the capture is a part of multiple stages capture on the same move, it's possible to capture also backward.  

2. When a pawn reaches the last line it is crowned to King. Kings are able to move both backward and forward and they're also able to capture both backward and forward. 
      
Our implementation is generic and can be easily expanded to even higher dimension boards that preserve the current game properties (The same rules, the first 3 lines of each side hold pieces).


                                	            ------ METHODOLOGIES ------

In this project we will use random and minimax algorithm with alpha-beta pruning to strategically play a game of checkers against a human opponent.  

● RANDOM: 
    Our baseline approach was to build a randomized player that picks each move from a set of possible moves. As the moves are picked randomly, that causes an irrational player which doesn't play by any strategy. A property of checkers is that one mistake is enough to assure the other player a sure win (even if it takes few dozens of moves). 

● MINIMAX:
The entire minimax algorithm has been coded from scratch. We considered optimization known as alpha-beta pruning and the algorithm is as follows: 

1. Have two values passed around the tree nodes:
➔   the alpha value which holds the best MAX value found.
➔   the beta value which holds the best MIN value found.
      
2. At MAX level, before evaluating each child path, compare the returned value with of the previous path with the beta value. If the value is greater than it abort the search for the current node.

3. At MIN level, before evaluating each child path, compare the returned value with of the previous path with the alpha value. If the value is lesser than it abort the search for the current node. 


	                                            ------ EVALUAION FUNCTIONS ------

1. OPENING-MIDDLEGAME EVALUATION FUNCTIONS  
We will be using different heuristic functions to see how favorable a particular game state is for our bot. The heuristics are based on the following factors:
a. The number of pieces of both the system and the opponent. 
b. The number of kings of both the players. 
c. Whether or not the move will result in expulsion of opponent’s piece. 
d. Whether the move will result in an enemy jump.
  
2. ENDING EVALUATION FUNCTIONS  
The game can end with two possible cases: 

  1. One player kills all checkers of other player In this case, if all the checkers of one player die, the opponent player  wins. 
  
  2. Game is stuck with same moves and no attacks are being made In case where there are no attacks by either of the players and moves exceed a certain limit, we count checkers for each player.
  a. WHITE WINS: Number of white checkers> Number of black checkers
  b. BLACK WINS: Number of white checkers< Number of black checkers
  c. DRAW: Number of white checkers = Number of black checkers

 
                                            	------ EXPERIMENTAL SETUP ------

In order to make our gaming experience more interesting for the user, we created different modes for the user to play in. The following are the different modes: 

● HUMAN VS ROBOT 
There are two possible cases when human vs bot game is played. They are as follows: 
    
1. HUMAN VS. MINIMAX ROBOT 
  In this scenario the user plays against an artificially intelligent which presents a good challenge to the user. 
  
2. HUMAN VS. RANDOM ROBOT 
  For those who don’t like a challenge and would much rather win the game easily, we created a bot which does not apply any algorithm to improve its performance, rather, it selects a random move from the available moves and plays without any sound logic following no methodology. This makes it easier for the user to win. The statistics have been provided in the pages to come.   

● ROBOT VS ROBOT 
    In order to further test the performance of the artificially intelligent bot we had created, we introduced the option to observe two bots competing against each other. The different variants of this are mentioned as follows: 
    
1. MINIMAX BOT VS. MINIMAX BOT 
   In this variant, the two artificially intelligent bots will go head to head against each other in attempts to outsmart the other one. 

2. RANDOM BOT VS. RANDOM BOT 
   As the name suggests, two bots functioning without any fixed guidelines or principles will compete against each other. 

3. RANDOM BOT VS. MINIMAX BOT 
   The randomly functioning bot will compete against one that is working based on a smart algorithm. 


                                            	------ IMPLEMENTATION ------
 
● The board – we chose to implement the board as a matrix (dimension X dimension). We think that this is the most logical way to do it and it will also make the GUI making process a bit simpler. 

● The square - or each game stage there is an array of pieces for both players. This is for knowing when the game ends, if the move if legal and other various issues.  

● The checker - Checker has its own class with its own attributes such as its coordinates and some boolean values. 

● The move – a class representing a move in the game. Contains more than just the Src and the Dest, but also all the data we need. 

● AI functions - Rest involves various functions that help in the working of random and artificial bots.


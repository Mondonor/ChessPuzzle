# ChessPuzzle
This is a proposed solution to a generalization of a popular chess puzzle found online recently.

The basic gist of the puzzle is:
You have a chessboard with each square having a coin on it, either heads or tails.
A Warden places a key underneath one of the coins such that you know where it is.
You get to flip one coin, and someone else who didn't see the key hidden must be able to see the board and know where the key is.

One elegant solution using 6th dimensional mod - 2 space can be found here: https://github.com/mwerner640/chess_puzzle

I wish to address this puzzle from a different perspective, however.

My solution is based on the basic assumptions:
1) You must have rules defined between yourself and your partner beforehand such that with 1 coin flip you can 
   point out the position of the key no matter where it is.
2) The positional information will be gotten across through some binary number which will be calculated by considering
   the states (heads or tails) of the coins on the board.
3) The board is square, with n squares per side. (We will see later that in principle my solution doesn't rely on it having this geometry,
   but for the sake of visualization I will use this assumption going forward).
   
From these assumptions, one can conclude:
1) The number of 'bits' required to relay this positional data is found by: bits >= log(base2)(n^2). We will work with the minimum integer.
2) To account for any starting position of the key / randomized starting condition of the coins, one must, with one coin flip, be able to
   uniquely change any specific bit (or any combination of bits) in the calculated binary number representing the key's position, as calculated by the state of the chessboard.
3) The number of unique changes one must be able to make can be found by: sum (k = 0, number of bits) {(number of bits) CHOOSE (k)}.
4) This gives us the condition on which this puzzle is solvable. The number of squares on the board must be AT LEAST the number of 
   unique changes possbile to the binary number representing the key's position, so for our square geometry: n ^ 2 >= sum (k = 0, number of bits) {(number of bits) CHOOSE (k)}.
5) From our Possibility Condition, if one calculates all n's for which it is possible up through n = 10000, one sees that only n's which are
   integer exponents of 2 have possible solutions, although I have yet to produce a rigorous proof showing this always must be the case.
   
With all of these principles and assumptions laid out, I constructed a simple script utilizing pygame which produces a randomized starting 
state of size specified by user-chosen n, generates the rules for which these states calculate a binary number which can properly point
out the key's position, and given a randomized starting key position finds the coin one must flip in order to make the calculated binary
number match the actual coin's position (some of this information is printed to the console).

Controls are:
'a' to generate the random coin states and key position
's' to generate the solution, and automatically applies the solution 2 seconds later to show that it works
'q' to quit
'r' to restart, if one desires to choose a new n

I will be fixing the UI and specific details in the program soon.

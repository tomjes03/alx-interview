In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n) Returns an integer If n is impossible to achieve, return 0 Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

Just like the divide and conquer algorithm, dynamic programming solves problems by combining the solutions to sub-problems. Divide and conquer algorithms partition the problem into independent sub-problems to solve the sub-problems recursively and then combine their solutions to solve the original problem. In contrast, dynamic programming is applicable when the sub-problem is not independent, that is when sub-problems share sub-problems. Therefore, a dynamic programming algorithm solves every sub-problem just once and then saves its answers in a table, thereby avoiding the work of recomputing the answer every time the subproblem is encountered.

The development of a dynamic programming algorithm can be broken into the sequence of four steps:

Characterize the structure of an optimal solution Recursively define the value of the optimal solution Compute the value of an optimal solution in a bottom-up fashion Construct an optimal solution from computed information Dynamic programming algorithm is designed in a way to optimize the given problem to get output by combining the solutions of sub-problems and appearing to the “the principle of optimality”.

What is the Principle of Optimality? The dynamic programming algorithm obtains the solution using the principle of optimality. The principle of optimality states that “ in an optimal sequence of decisions or choices, each subsequence must also be optimal”. When it is not possible to apply the principle of optimality it is almost impossible to obtain the solution using the dynamic programming approach.

The principle of optimality: “If k is a node on the shortest path from i to j, then the part of the path from i to k, and the part from k to i, must also be optimal.”

The project was done as part of a computer simulation course. In the project, I simulated filling a surface (board) with square blocks of certain dimensions.

At the very beginning, we have a surface with dimensions 𝑤 × 𝑤, and we can input the board dimensions ourselves. The parameters of our problem are: the variable 𝑤 (size of the surface), the number of iterations to complete the game, different types of squares (2 × 2, 3 × 3, 4 × 4), and the number of iterations after which they disappear. The type of square and the number of iterations are randomly drawn from a uniform distribution.

The decision variable is whether we will place a square on the board. We place it in the first available place that fits, starting from the upper left corner of the surface. In the first case, we discard blocks when there is no more room on the board, and in the second case, when there is no more room on the board, we wait for iterations to pass before placing the block.

The problem is that we want to occupy as much of our surface as possible. The objective function is 𝑓 = max (∑𝑝 − ∑𝑘), where the matrix p is the number of filled fields, and we add to it after each iteration, and the matrix k is the number of filled fields of the squares that we did not place on the board.

Due to the fact that only the results from the first approach came from a normal distribution, we used the Wilcoxon test. The null hypothesis was that the second approach is better than the first, and the alternative hypothesis was that the first approach is better than the second (the objective function achieves a higher score). After conducting the test, we reject the null hypothesis at a significance level of p = 2.19e-06.

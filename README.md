# Conway's Game of Life
A robust solution to the classic coding challenge Conway's Game of Life

## About Conway's rules:

Rules to Conway's game of life:
    1. Cells next to exactly 3 alive cells will become alive in the next iteration.
    2. Each cell with 1 or fewer alive neighbours will die in the next iteration.
    3. Each cell with 4 or more live neighbours will die in the next iteration.
    4. Survival: if alive, a cell with 2 or 3 neighbours will persist.
    
Algorithm:
    1. initialize a random matrix.
    2. initialize a random matrix representing state T+1.
    3. iterate through each cell in initial matrix applying conway's rules to matrix T+1.
    4. set next matrix to initial matrix.
    5. repeat for all iterations of the game.    

## Initialized random game
```
1 0 1 0 0 1 1 0
1 1 1 1 0 0 1 0
0 0 1 1 1 0 1 1
1 1 1 1 0 0 1 0
1 0 1 0 0 0 0 0
1 1 0 0 0 1 1 1
0 1 0 1 0 1 1 1
1 1 1 0 0 1 1 1
```

## ..after 1 iteration
```
0 1 0 0 0 0 1 0
1 1 0 1 0 0 1 0
0 1 1 0 0 0 1 0
1 1 0 1 0 0 0 0
1 0 0 0 0 0 0 0
1 1 0 0 0 1 1 1
1 1 1 0 0 1 0 1
0 1 0 0 0 1 1 1
```

## ..after 2 iterations
```
0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 0
1 1 0 1 0 0 0 0
1 1 1 0 0 0 0 0
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 1
1 0 0 0 0 1 0 1
0 0 0 0 0 1 1 1
```
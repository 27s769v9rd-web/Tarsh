"""
  File: spiral.py
  Description:

  Student Name: Jeff Zheng
  Student UT EID: jrz554

  Partner Name: N/A
  Partner UT EID: N/A

  Course Name: CS 313E
  Unique Number: 54150
  Date Created: Sep 11
  Date Last Modified: Sep 11

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
    
 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

import math


def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""
  #Setup
  if dim % 2 == 0:
    dim += 1
  grid = [[0] * dim for _ in range(dim)]
  #Put a 1 in the center
  row = col = dim // 2
  grid[row][col] = 1
  
  num = 1
  total = dim * dim

  #Direction cycle
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  d = 0
  step = 1

  #Keep filling
  while num < total:
    for i in range(2):
      drow, dcol = directions[d]
      for j in range(step):
        row += drow
        col += dcol
        if 0 <= row < dim and 0 <= col < dim:
          num += 1
          grid[row][col] = num
          if num == total:
            return grid
      d = (d + 1) % 4
    step += 1
  return grid

def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
  
  dim = len(grid)

  #locate val in the grid
  position = None
  for i in range(dim):
    for j in range(dim):
      if grid[i][j] == val:
        pos = (i,j)
        break
    if pos i not None:
      Break
  if pos is None:
    return 0
  #scan the blocks around val and add it
  row, col = pos
  total = 0
  for i in range(row - 1, raw + 2):
    for j in range(col - 1, col + 2):
      if 0 <= i < dim and 0 <= j < dim and (i, j) != (row, col):
        total += grid[i]][j]
  return total

def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()

print("enter your config for the sudoku grid, 0 equals empty")
A1 = int(input("A1"))
A2 = int(input("A2"))
A3 = int(input("A3"))
A4 = int(input("A4"))
A5 = int(input("A5"))
A6 = int(input("A6"))
A7 = int(input("A7"))
A8 = int(input("A8"))
A9 = int(input("A9"))
B1 = int(input("B1"))     
B2 = int(input("B2"))
B3 = int(input("B3"))
B4 = int(input("B4"))
B5 = int(input("B5"))
B6 = int(input("B6"))
B7 = int(input("B7"))
B8 = int(input("B8"))
B9 = int(input("B9"))
C1 = int(input("C1"))
C2 = int(input("C2"))
C3 = int(input("C3"))
C4 = int(input("C4"))
C5 = int(input("C5"))
C6 = int(input("C6"))
C7 = int(input("C7"))
C8 = int(input("C8"))
C9 = int(input("C9"))
D1 = int(input("D1"))
D2 = int(input("D2"))
D3 = int(input("D3"))
D4 = int(input("D4"))
D5 = int(input("D5"))
D6 = int(input("D6"))
D7 = int(input("D7"))
D8 = int(input("D8"))
D9 = int(input("D9"))
E1 = int(input("E1"))
E2 = int(input("E2"))
E3 = int(input("E3"))
E4 = int(input("E4"))
E5 = int(input("E5"))
E6 = int(input("E6"))
E7 = int(input("E7"))
E8 = int(input("E8"))
E9 = int(input("E9"))
F1 = int(input("F1"))
F2 = int(input("F2"))
F3 = int(input("F3"))
F4 = int(input("F4"))
F5 = int(input("F5"))
F6 = int(input("F6"))
F7 = int(input("F7"))
F8 = int(input("F8"))
F9 = int(input("F9"))
G1 = int(input("G1"))
G2 = int(input("G2"))
G3 = int(input("G3"))
G4 = int(input("G4"))
G5 = int(input("G5"))
G6 = int(input("G6"))
G7 = int(input("G7"))
G8 = int(input("68"))
G9 = int(input("G9"))
H1 = int(input("H1"))
H2 = int(input("H2"))
H3 = int(input("H3"))
H4 = int(input("H4"))
H5 = int(input("H5"))
H6 = int(input("H6"))
H7 = int(input("H7"))
H8 = int(input("H8"))
H9 = int(input("H9"))
I1 = int(input("I1"))
I2 = int(input("I2"))
I3 = int(input("I3"))
I4 = int(input("I4"))
I5 = int(input("I5"))
I6 = int(input("I6"))
I7 = int(input("I7"))
I8 = int(input("I8"))
I9 = int(input("I9"))



M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
grid = [[A1, A2, A3, A4, A5, A6, A7, A8, A9],
        [B1, B2, B3, B4, B5, B6, B7, B8, B9],
    [C1, C2, C3, C4, C5, C6, C7, C8, C9],
    [D1, D2, D3, D4, D5, D6, D7, D8, D9],
    [E1, E2, E3, E4, E5, E6, E7, E8, E9],
    [F1, F2, F3, F4, F5, F6, F7, F8, F9],
    [G1, G2, G3, G4, G5, G6, G7, G8, G9],
    [H1, H2, H3, H4, H5, H6, H7, H8, H9],
    [I1, I2, I3, I4, I5, I6, I7, I8, I9]]
 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")
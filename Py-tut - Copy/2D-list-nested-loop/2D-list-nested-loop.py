GRID = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(GRID[1][2])
print(GRID[0][0])
print(GRID[3][0])

for row in GRID:
    print(row)

for row in GRID:
    for column in row:
        print(column)
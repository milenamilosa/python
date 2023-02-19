# .append
# name_of_variable.append(what_u_add) = add to existing space

# .extend

grid = []

for row in range(5):
    new_row = []
    for col in range(5):
        new_row.append((row, col))
    grid.append(new_row)

for row in grid:
    print(row)
print("\n")

grid = []

for row in range(5):
    new_row = []
    for col in range(5):
        new_row = new_row + [(row, col)]
    grid = grid + [new_row]

for row in grid:
    print(row)
print("\n")

matrix = []

for row in range(5):
    new_row = []
    for col in range(5):
        new_row.append(row*col)
    matrix.append(new_row)
for row in matrix:
    print (row)
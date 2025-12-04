def check_roll(i: int, j: int) -> int:
    adj = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if ((i + x) >= 0 and (j + y) >= 0) and ((i + x) < len(matrix) and (j + y) < len(matrix[0])):
                if (x != 0) or (y != 0):
                    if (matrix[i + x][j + y] == "@"):
                        adj += 1
    return adj

if __name__ == "__main__":

    file = open("./4 December/input.txt", "r")
    matrix = [list(row.strip()) for row in file]
    rolls = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "@":
                if check_roll(i, j) < 4:
                    rolls += 1
            
    print(f"Total accesible rolls: {rolls}")
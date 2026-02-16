from pathlib import Path


def create(filepath):
    matrix = []
    with open(filepath, "r") as f:
        for line in f:
            row = list(line.strip())
            matrix.append(row)

    Queen = len(matrix)
    return matrix, Queen



filedir = Path(__file__).parent
filename = input("Enter file name")
filepath = filedir / 'test' / (filename + ".txt")

matrix, Queen = create(filepath)

def plsSolveQueen(num):
    matrixforthis = matrix
    Queenpos = [[-1, -1]*Queen for _ in range(Queen)]

    def sameblock(a, b, n):
        for i in range(n+1):
            if Queenpos[i][1] == a and Queenpos[i][2] == b:
                return True
        return False

    def findPos(n):
        if n == num:
            for i in range(Queen):
                for j in range(Queen):
                    if sameblock(i, j):
                        continue
                    else:
                        print("yes")
        else:
            for i in range(Queen):
                for j in range(Queen):
                    if sameblock(i, j, n):
                        continue
                    else:
                        Queenpos[n][1] = i
                        Queenpos[n][2] = j
                        findPos(n)
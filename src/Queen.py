from pathlib import Path
import time


def create(filepath):
    matrix = []
    with open(filepath, "r") as f:
        for line in f:
            row = list(line.strip())
            matrix.append(row)

    Queen = len(matrix)
    return matrix, Queen


def plsSolveQueen(num, matrix, Queen):
    matrixforthis = matrix
    Queenpos = [[-1, -1] for _ in range(Queen)]

    def sameblock(a, b, n):
        for i in range(n):
            if Queenpos[i][0] == a and Queenpos[i][1] == b:
                return True
        return False

    def findPos(n):
        if n == num:
            return checkQueen()

        else:
            for i in range(Queen):
                for j in range(Queen):
                    if sameblock(i, j, n):
                        continue
                    else:
                        Queenpos[n][0] = i
                        Queenpos[n][1] = j
                        if findPos(n+1):
                            return True
            return False

    def checkQueen():
        for i in range(Queen):
            for j in range(i + 1, Queen):
                if Queenpos[i][0] == Queenpos[j][0]:
                    return False
                if Queenpos[i][1] == Queenpos[j][1]:
                    return False
                if abs(Queenpos[i][0] - Queenpos[j][0]) == 1 and abs(Queenpos[i][1] - Queenpos[j][1]) == 1:
                    return False
                if matrixforthis[Queenpos[i][0]][Queenpos[i][1]] == matrixforthis[Queenpos[j][0]][Queenpos[j][1]]:
                    return False
        return True
    
    if findPos(0):
        return Queenpos
    else:
        return None


def print_solution(queenpos, matrix):
    if queenpos is None:
        print("No solution found")
        return
    
    size = len(matrix)
    result = [row[:] for row in matrix]
    
    for i, (row, col) in enumerate(queenpos):
        result[row][col] = 'Q'
    
    print("\nSolution:")
    for row in result:
        print(' '.join(row))
    print("\nQueen positions:")
    for i, (row, col) in enumerate(queenpos):
        print(f"Queen {i+1}: ({row}, {col})")


if __name__ == "__main__":
    filedir = Path(__file__).parent
    filename = input("Enter file name:")
    filepath = filedir / 'test' / (filename + ".txt")

    matrix, Queen = create(filepath)

    # Run and time the solver
    start_time = time.time()
    solution = plsSolveQueen(Queen, matrix, Queen)
    end_time = time.time()

    print_solution(solution, matrix)
    print(f"\nTime elapsed: {end_time - start_time:.4f} seconds")
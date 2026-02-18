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

def checkMatrix(matrix):
    numrows = len(matrix)
    
    for row in matrix:
        if len(row) != numrows:
            return False
        
    colors = set()
    
    for row in matrix:
        for cell in row:
            if not cell.isupper() or not cell.isalpha():
                return False
            colors.add(cell)
    
    if len(colors) != numrows:
        return False
    
    return True
    

def printSolution(queenpos, matrix):
    if queenpos is None:
        print("No solution found")
        return
    
    size = len(matrix)
    result = [row[:] for row in matrix]
    
    for i, (row, col) in enumerate(queenpos):
        result[row][col] = 'Q'
    
    for row in result:
        print(''.join(row))
    print("\nQueen positions:")
    for i, (row, col) in enumerate(queenpos):
        print(f"Queen {i+1}: ({row}, {col})")


def saveSolutionToFile(queenpos, matrix, filename):
    if queenpos is None:
        output_content = "No solution found\n"
    else:
        output_lines = []

        size = len(matrix)
        result = [row[:] for row in matrix]
        
        for i, (row, col) in enumerate(queenpos):
            result[row][col] = 'Q'
        
        for row in result:
            output_lines.append(''.join(row))
        
        output_content = '\n'.join(output_lines)
    
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / f"{filename}Solution.txt"
    
    with open(output_file, 'w') as f:
        f.write(output_content)


def plsSolveQueen(num, matrix, Queen):
    matrixforthis = matrix
    Queenpos = [[-1, -1] for _ in range(Queen)]
    iteration = 0



    def sameblock(a, b, n):
        for i in range(n):
            if Queenpos[i][0] == a and Queenpos[i][1] == b:
                return True
        return False

    def findPos(n):
        nonlocal iteration
        if n == num:
            iteration += 1
            if iteration % 1000 == 0:
                printSolution(Queenpos, matrix)
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
        return Queenpos, iteration
    else:
        return None, iteration
    
    
while  True:
    filedir = Path(__file__).parent
    filename = input("Enter file name:")
    filepath = filedir / 'test' / (filename + ".txt")

    matrix, Queen = create(filepath)
    if checkMatrix(matrix):
        break
    else:
        print("Input a valid board!\n")

startTime = time.time()
solution, iteration = plsSolveQueen(Queen, matrix, Queen)
endTime = time.time()

printSolution(solution, matrix)
print(iteration)
print(f"\nTime taken: {endTime - startTime:.4f} seconds")

saveSolutionToFile(solution, matrix, filename)
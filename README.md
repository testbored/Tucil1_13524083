# LinkedIn Queens Puzzle Solver

## Overview
This program solves the **LinkedIn Queens Puzzle** using a brute-force  algorithm. The puzzle requires placing N queens on an N×N board such that:
- No two queens attack each other (same row, column, or adjacent diagonal)
- No two queens occupy the same color/region

## Requirements
- **Python 3.11+**
- **Git** (to clone the repository)
- **IDE or Text Editor** (e.g., VS Code, PyCharm, Sublime Text)
- No additional dependencies (uses only standard library: `pathlib` and `time`)

## Program Structure

### Files
- `src/Queen.py` - Main solver program
- `src/test/` - Directory containing test cases for to run the program
- `src/output/` - Directory containing solutions for each test case
- `src/test/` - Directory containing both solutions and test case that was used for testing


### Input Format
Test files should be text files with an N×N grid where each cell contains a letter representing a region/color. Example (4×4):
```
AAAA
BBCC
BBCC
DDDD
```

## Setup

### Clone the Repository
```bash
git clone https://github.com/testbored/Tucil1_13524083.git
cd Tucil1_13524083
```

### Open in IDE
Open the project folder in your preferred IDE:
- **VS Code**: `code .`
- **PyCharm**: File → Open → Select folder
- Or manually open the folder in your IDE

## How to Run

### Step 1: Open Terminal
Navigate to the project root directory:
```bash
cd path/to/Tucil1_13524083
```

### Step 2: Run the Program
```bash
python src/Queen.py
```

### Step 3: Enter Test File Name
When prompted, enter the filename without the `.txt` extension. For example:
```
Enter file name: queens_test_4x4
```


## Creating Custom Test Cases
Create a new `.txt` file in `src/test/` with:
- Grid size: N×N
- Each cell: single letter representing a region
- Save with extension `.txt`



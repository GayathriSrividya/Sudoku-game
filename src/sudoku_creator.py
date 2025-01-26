import random
import json
from utils import write_markdown, can_place_number, format_board
from sudoku_solver import solve


def generate_full_solution():
    """
    Generates a complete valid Sudoku solution by:
    * Placing a few random initial numbers
    * Using existing sudoku solver to fill in the rest
    * Returns a 9x9 solved Sudoku board
    """
    board = [[0] * 9 for _ in range(9)]
    initial_numbers = 9
    for _ in range(initial_numbers):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while board[row][col] != 0 or not can_place_number(board, row, col, num):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    solve(board)
    return board


def remove_numbers(board, num_to_remove=40):
    attempts = num_to_remove
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            attempts -= 1
    return board

def create_sudoku_puzzle(options):
    """
    * Creates a Sudoku puzzle by generating a full solution and removing numbers.
    * The difficulty is determined by the number of cells removed.
    * Writes the puzzle to a file.
    """
    num_to_remove = options.get('cells_to_remove')
    file_path = options.get('question_file')
    full_board = generate_full_solution()
    puzzle_board = remove_numbers(full_board, num_to_remove)
    write_markdown(file_path, puzzle_board, "Your puzzle")
    print("\nYour puzzle:\n")
    print(format_board(puzzle_board))
    print(f"\nPuzzle has been saved to {file_path}")

def setup_options():
    with open('config.json', 'r') as file:
        config = json.load(file)
    
    for num, level in config['levels'].items():
        print(f"{num}: {level}")
    
    choice = input("Choice (default: 1): ").strip()
    level = config['levels'].get(choice, 'medium')
    
    return {
        'question_file': config['question_file'],
        'cells_to_remove': config['cells_to_remove'][level]
    }

if __name__ == "__main__":
    try:
        options = setup_options()
        create_sudoku_puzzle(options)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

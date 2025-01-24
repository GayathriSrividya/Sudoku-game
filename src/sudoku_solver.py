import time
import json
from utils import (
    read_markdown,
    validate_board,
    write_markdown,
    get_possibilities,
    analyse_possibilities,
)


def solve(grid):
    previous_attempts = []

    while True:
        cell_options = get_possibilities(grid)
        if len(cell_options) == 0:
            break

        row, col, option_count, valid_nums = cell_options[0]

        if option_count == 0:
            if not previous_attempts:
                return False

            found_next = False
            while previous_attempts and not found_next:
                last_row, last_col, last_nums, index = previous_attempts.pop()
                if index + 1 < len(last_nums):
                    grid[last_row][last_col] = last_nums[index + 1]
                    previous_attempts.append((last_row, last_col, last_nums, index + 1))
                    found_next = True
                else:
                    grid[last_row][last_col] = 0

            if not found_next:
                return False
            continue

        grid[row][col] = valid_nums[0]
        previous_attempts.append((row, col, valid_nums, 0))

    return True


def initial_validation(read_path):
    sudoku_board = read_markdown(read_path)
    is_valid_question = validate_board(sudoku_board)
    if is_valid_question:
        analyse_possibilities(sudoku_board)
        return sudoku_board, True
    else:
        return [], False


if __name__ == "__main__":
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        read_path = config["question_file"]
        write_path = config["answer_file"]
        start_time = time.time()
        sudoku_board, is_valid_board = initial_validation(read_path)
        if is_valid_board:
            solved = solve(sudoku_board)
            if solved:
                write_markdown(write_path, sudoku_board, "Answer")
                print("Sudoku solved successfully! Check out answer in answer.md")
                end_time = time.time()
                print(f"Execution time: {end_time - start_time:.6f} seconds")
            else:
                print("Failed to solve the Sudoku!")
        else:
            print("Invalid puzzle!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

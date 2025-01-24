import re


def read_markdown(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    board = []
    in_puzzle = False
    for line in content.splitlines():
        if "Your puzzle:" in line:
            in_puzzle = True
            continue
        if in_puzzle and re.match(r"^[0-9 x|]+$", line):
            line = line.replace("|", "").strip()
            board.append([int(num) if num.isdigit() else 0 for num in line.split()])
    return board


def write_markdown(file_path, board, heading_text):
    with open(file_path, "w") as file:
        file.write("## {}:\n\n```\n".format(heading_text, "Answer"))
        for i, row in enumerate(board):
            line = " ".join(str(num) if num != 0 else "x" for num in row)
            line_with_pipes = " | ".join([line[:5], line[6:11], line[12:]])
            file.write(line_with_pipes + "\n")
            if i == 2 or i == 5:
                file.write("------+------+------\n")
        file.write("```\n")


def get_subgrid(board, row, col):
    grid_row_start = int(row // 3) * 3
    grid_col_start = int(col // 3) * 3
    subgrid = []
    for i in range(grid_row_start, grid_row_start + 3):
        for j in range(grid_col_start, grid_col_start + 3):
            subgrid.append(board[i][j])
    return subgrid


def can_place_number(board, row, col, num):
    subgrid = get_subgrid(board, row, col)
    if num in subgrid or num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    return True


def get_possibilities(board):
    possibilities = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                possible_values = [
                    num
                    for num in range(1, 10)
                    if can_place_number(board, row, col, num)
                ]
                possibilities.append((row, col, len(possible_values), possible_values))
    possibilities.sort(key=lambda x: (x[2], x[0], x[1]))
    return possibilities


def analyse_possibilities(board):
    possibilities = get_possibilities(board)
    for row, col, _, possible_values in possibilities:
        if len(possible_values) == 1:
            value = possible_values[0]
            board[row][col] = value


def has_duplicates(numbers):
    valid_nums = [n for n in numbers if n != 0]
    return len(valid_nums) != len(set(valid_nums))


def validate_board(board):
    for row in board:
        if has_duplicates(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if has_duplicates(column):
            return False

    for row in range(3):
        for col in range(3):
            if has_duplicates(get_subgrid(board, row * 3, col * 3)):
                return False

    return True

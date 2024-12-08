import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns the starting state of the board.
    """
    return [[EMPTY] * 3 for _ in range(3)]


def player(board):
    """
    Returns the player who has the next turn on the board.
    """
    moves = sum(cell != EMPTY for row in board for cell in row)
    return X if moves % 2 == 0 else O


def actions(board):
    """
    Returns a set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action.")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    if result == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board), None
        value = float('-inf')
        best_action = None
        for action in actions(board):
            new_value, _ = min_value(result(board, action))
            if new_value > value:
                value = new_value
                best_action = action
                if value == 1:  # Pruning
                    break
        return value, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        value = float('inf')
        best_action = None
        for action in actions(board):
            new_value, _ = max_value(result(board, action))
            if new_value < value:
                value = new_value
                best_action = action
                if value == -1:  # Pruning
                    break
        return value, best_action

    return max_value(board)[1] if current_player == X else min_value(board)[1]

def is_valid_chess_board(board):
    for space in board.keys():
        if len(space) != 2:
            return False

        if space[0] < '1' or space[0] > '8':
            return False
        if space[1] < 'a' or space[1] > 'h':
            return False

    counter = {}
    for piece in board.values():
        if len(piece) < 2:
            return False

        player = piece[0]
        if player != 'w' and player != 'b':
            return False

        counter.setdefault(player, 0)
        counter[player] += 1

        if piece[1:] not in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king'):
            return False

        counter.setdefault(piece, 0)
        counter[piece] += 1

    for player in ('w', 'b'):
        if counter.get(player + 'king', 0) != 1:
            return False

        if counter.get(player, 0) > 16:
            return False

        if counter.get(player + 'pawn', 0) > 8:
            return False

        if counter.get(player + 'knight', 0) > 2:
            return False

        if counter.get(player + 'bishop', 0) > 2:
            return False

        if counter.get(player + 'rook', 0) > 2:
            return False

        if counter.get(player + 'queen', 0) > 1:
            return False

    return True

if __name__ == '__main__':
    assert is_valid_chess_board({
        '1h': 'bking',
        '6c': 'wqueen',
        '2g': 'bbishop',
        '5h': 'bqueen',
        '3e': 'wking'
    }) == True

    assert is_valid_chess_board({
        '1a': 'wrook',
        '1b': 'wknight',
        '1c': 'wbishop',
        '1d': 'wqueen',
        '1e': 'wking',
        '1f': 'wbishop',
        '1g': 'wknight',
        '1h': 'wrook',
        '2a': 'wpawn',
        '2b': 'wpawn',
        '2c': 'wpawn',
        '2d': 'wpawn',
        '2e': 'wpawn',
        '2f': 'wpawn',
        '2g': 'wpawn',
        '2h': 'wpawn',
        '8a': 'brook',
        '8b': 'bknight',
        '8c': 'bbishop',
        '8d': 'bqueen',
        '8e': 'bking',
        '8f': 'bbishop',
        '8g': 'bknight',
        '8h': 'brook',
        '7a': 'bpawn',
        '7b': 'bpawn',
        '7c': 'bpawn',
        '7d': 'bpawn',
        '7e': 'bpawn',
        '7f': 'bpawn',
        '7g': 'bpawn',
        '7h': 'bpawn',
    }) == True

    assert is_valid_chess_board({
        '1e': 'wking',
        '2a': 'wpawn',
        '2b': 'wpawn',
        '2c': 'wpawn',
        '2d': 'wpawn',
        '2e': 'wpawn',
        '2f': 'wpawn',
        '2g': 'wpawn',
        '2h': 'wpawn',
        '3h': 'wpawn',
        '8e': 'bking',
    }) == False

    assert is_valid_chess_board({
        '1e': 'wking',
        '2a': 'bpawn',
        '2b': 'bpawn',
        '2c': 'bpawn',
        '2d': 'bpawn',
        '2e': 'bpawn',
        '2f': 'bpawn',
        '2g': 'bpawn',
        '2h': 'bpawn',
        '3h': 'bpawn',
        '8e': 'bking',
    }) == False

    assert is_valid_chess_board({
        '9h': 'bking',
        '3e': 'wking'
    }) == False

    assert is_valid_chess_board({
        '1z': 'bking',
        '3e': 'wking'
    }) == False

    assert is_valid_chess_board({
        '1e': 'wking',
    }) == False

    assert is_valid_chess_board({
        '1z': 'bking',
        '3e': 'yking'
    }) == False

    assert is_valid_chess_board({
        '1z': 'bking',
        '3e': 'wgold'
    }) == False


def checkmate(board: str) -> str:
    try:
        rows = board.strip().split("\n")
        n = len(rows)

        if any(len(r) != n for r in rows):
            return "Error"

        king_pos = None
        for i in range(n):
            for j in range(n):
                if rows[i][j] == "K":
                    king_pos = (i, j)
                    break
            if king_pos:
                break

        if not king_pos:
            return "Error"

        ki, kj = king_pos

        rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]

        for di, dj in rook_dirs:
            i, j = ki+di, kj+dj
            while 0 <= i < n and 0 <= j < n:
                piece = rows[i][j]
                if piece != ".":
                    if piece in ("R", "Q"):
                        return "Success"
                    break
                i += di
                j += dj

        for di, dj in bishop_dirs:
            i, j = ki+di, kj+dj
            while 0 <= i < n and 0 <= j < n:
                piece = rows[i][j]
                if piece != ".":
                    if piece in ("B", "Q"):
                        return "Success"
                    break
                i += di
                j += dj

        pawn_attacks = [(1, -1), (1, 1)]
        for di, dj in pawn_attacks:
            i, j = ki+di, kj+dj
            if 0 <= i < n and 0 <= j < n:
                if rows[i][j] == "P":
                    return "Success"

        return "Fail"

    except Exception:
        return "Error"

# pylint: disable=invalid-name, missing-docstring, redefined-outer-name
# pylint: disable=no-else-return
# ref: https://www.hackerrank.com/challenges/queens-attack-2/problem
# diagonal movement of queen
# bot_right: -1, 1
# bot_left: -1, -1
# top_left: 1, -1
# top_right: 1, 1
# vertical & horizontal movement
# top: 1, 0, bottom: -1, 0; left: 0,-1, right: 0, 1

# i ---> row val
# j ---> col val
import math


def obs_direction(q_r, q_c, obs):
    """
    Obstacle in Queen's path
    Parameters
    ----------
    q_r: Queen's row position
    q_c: Queen's column position
    b_size: square board size, b_size X b_size
    obs: marked as obstacles in square board [row, col]
    Returns
    -------
    string, direction (vertical, horizontal, diagonal)
    """
    delta_r = abs(q_r - obs[0])
    delta_c = abs(q_c - obs[1])

    if delta_r == 0 and q_c > obs[1]:
        return "horizontal_left"
    elif delta_r == 0 and q_c < obs[1]:
        return "horizontal_right"
    elif delta_c == 0 and q_r > obs[0]:
        return "vertical_down"
    elif delta_c == 0 and q_r < obs[0]:
        return "vertical_up"
    elif delta_c == delta_r and (q_c - obs[1]) < 0 < (q_r - obs[0]):
        return "diagonal_bottom_right"
    elif delta_c == delta_r and (q_c - obs[1]) > 0 < (q_r - obs[0]):
        return "diagonal_bottom_left"
    elif delta_c == delta_r and (q_r - obs[0]) < 0 < (q_c - obs[1]):
        return "diagonal_top_left"
    elif delta_c == delta_r and (q_r - obs[0]) < 0 > (q_c - obs[1]):
        return "diagonal_top_right"


def max_diag_right_up(row, col, dim):
    move_count = 0
    up_lim = dim + 1
    # diagonal right up moves
    dru_i, dru_j = row + 1, col + 1
    while dru_i < up_lim and dru_j < up_lim:
        move_count += 1
        dru_i += 1
        dru_j += 1
    return move_count


def max_diag_left_up(row, col, dim):
    move_count = 0
    up_lim = dim + 1
    low_lim = 0
    # diagonal left up moves
    dlu_i, dlu_j = row + 1, col - 1
    while dlu_i < up_lim and dlu_j > low_lim:
        move_count += 1
        dlu_i += 1
        dlu_j -= 1
    return move_count


def max_diag_right_down(row, col, dim):
    move_count = 0
    up_lim = dim + 1
    low_lim = 0
    # diagonal right down moves
    drd_i, drd_j = row - 1, col + 1
    while drd_i > low_lim and drd_j < up_lim:
        move_count += 1
        drd_i -= 1
        drd_j += 1
    return move_count


def max_diag_left_down(row, col, dim):
    move_count = 0
    low_lim = 0
    # diagonal left down moves
    dld_i, dld_j = row - 1, col - 1
    while dld_i > low_lim and dld_j > low_lim:
        move_count += 1
        dld_i -= 1
        dld_j -= 1
    return move_count


def horizontal_left_moves(obs, q_r, q_c):
    """
    Possible move counts in horizontal left direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    hlo = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "horizontal_left":
            hlo.append(ob)
    # nearest to queen's position
    if not hlo:
        return q_c -1
    else:
        ed_val = []
        for coord in hlo:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = hlo[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[1] - q_c) - 1


def horizontal_right_moves(obs, q_r, q_c, n):
    """
    Possible move counts in horizontal right direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    n: board dimension
    Returns
    -------
    integer, total possible moves count
    """
    hro = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "horizontal_right":
            hro.append(ob)
    # nearest to queen's position
    if not hro:
        return n - q_c
    else:
        ed_val = []
        for coord in hro:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = hro[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[1] - q_c) - 1


def vertical_down_moves(obs, q_r, q_c):
    """
    Possible move counts in vertical down direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    vdo = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "vertical_down":
            vdo.append(ob)
    # nearest to Queen's position
    if not vdo:
        return q_r - 1
    else:
        ed_val = []
        for coord in vdo:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = vdo[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[0] - q_r) - 1


def vertical_up_moves(obs, q_r, q_c, n):
    """
    Possible move counts in vertical up direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    vuo = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "vertical_up":
            vuo.append(ob)
    # nearest to Queen's position
    if not vuo:
        return n - q_r
    else:
        ed_val = []
        for coord in vuo:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = vuo[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[0] - q_r) - 1


def diagonal_bottom_right_moves(obs, q_r, q_c, n):
    """
    Possible move counts in diagonal bottom right direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    dbro = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "diagonal_bottom_right":
            dbro.append(ob)
    # nearest to Queen's position
    if not dbro:
        return max_diag_right_down(q_r, q_c, n)
    else:
        ed_val = []
        for coord in dbro:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = dbro[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[1] - q_c) - 1


def diagonal_bottom_left_moves(obs, q_r, q_c, n):
    """
    Possible move counts in diagonal bottom left direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    dblo = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "diagonal_bottom_left":
            dblo.append(ob)
    # nearest to Queen's position
    if not dblo:
        return max_diag_left_down(q_r, q_c, n)
    else:
        ed_val = []
        for coord in dblo:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = dblo[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[1] - q_c) - 1


def diagonal_top_left_moves(obs, q_r, q_c, n):
    """
    Possible move counts in diagonal top left direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    dtlo = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "diagonal_top_left":
            dtlo.append(ob)
    # nearest to Queen's position
    if not dtlo:
        return max_diag_left_up(q_r, q_c, n)
    else:
        ed_val = []
        for coord in dtlo:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = dtlo[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return abs(effective_obs[1] - q_c) - 1


def diagonal_top_right_moves(obs, q_r, q_c, n):
    """
    Possible move counts in diagonal top right direction
    Parameters
    ----------
    obs: list, obstacles coordinates (row, col)
    q_r: Queen's row position (y)
    q_c: Queen's col position (x)
    Returns
    -------
    integer, total possible moves count
    """
    dtro = []
    for ob in obs:
        if obs_direction(q_r, q_c, ob) == "diagonal_top_right":
            dtro.append(ob)
    # nearest to Queen's position
    if not dtro:
        return max_diag_right_up(q_r, q_c, n)
    else:
        ed_val = []
        for coord in dtro:
            ed_val.append(euclidean_distance(q_r, q_c, coord))
        effective_obs = dtro[ed_val.index(min(ed_val))]

        # total possible moves from Queen's position to effective_obs
        return effective_obs[1] - q_c - 1


def euclidean_distance(q_r, q_c, obs):
    """
    Obstacle in Queen's path
    Parameters
    ----------
    q_r: Queen's row position
    q_c: Queen's column position
    obs: list, marked as obstacles in square board [row, col]
    Returns
    -------
    float, euclidean distance between (q_c, q_r) and obs
    """
    return math.sqrt(math.pow((obs[1] - q_c), 2) + math.pow((obs[0] - q_r), 2))


def test_case(file_name):
    with open(file_name, 'r') as tc:
        data = tc.readlines()
        nk = data[0].split()
        n = int(nk[0])
        r_qc_q = data[1].split()
        r_q, c_q = int(r_qc_q[0]), int(r_qc_q[1])

        obs = []
        for d in data[2:]:
            temp = list(map(int, d.split()))
            obs.append(temp)
    return (n, r_q, c_q, obs)


def queens_attack(obs, q_r, q_c, n):
    """
    Queen's possible movement in dim x dim chess board.
    Parmeters
    ---------
    row_pos: Queen's row position
    col_pos: Queen's col position
    dim: square board size n x n
    Returns
    -------
    integer, number of possible moves
    """
    moves = []
    # breakpoint()
    moves.append(horizontal_left_moves(obs, q_r, q_c))
    moves.append(horizontal_right_moves(obs, q_r, q_c, n))
    moves.append(vertical_down_moves(obs, q_r, q_c))
    moves.append(vertical_up_moves(obs, q_r, q_c, n))
    moves.append(diagonal_top_left_moves(obs, q_r, q_c, n))
    moves.append(diagonal_top_right_moves(obs, q_r, q_c, n))
    moves.append(diagonal_bottom_right_moves(obs, q_r, q_c, n))
    moves.append(diagonal_bottom_left_moves(obs, q_r, q_c, n))
    return sum(moves)


if __name__ == "__main__":
    file_name = "./queensAttackTestCase13.txt"
    n, q_r, q_c, obs = test_case(file_name)
    assert queens_attack(obs, q_r, q_c, n) == 307303
    n, q_r, q_c = 5, 4, 3
    obs = [[5, 5], [4, 2], [2, 3]]
    assert queens_attack(obs, q_r, q_c, n) == 10

# pylint: disable=invalid-name
"""
Matrix Layer Rotation
Ref: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
"""

import itertools


def matrix(rows, cols):
    mat = []
    start = 1
    end = cols + 1
    for _ in range(rows):
        temp = [i for i in range(start, end)]
        mat.append(temp)
        start += cols
        end += cols
    return mat


# find concentric rings in matrix
def concentric_rings(rows, cols, mat):
    """
    Imagine matrix as a concentric rings
    Parameters
    ----------
    matrix: array of rows having cols elements
    rows: number of rows in matrix
    cols: number of cols in matrix
    Returns
    -------
    list of concentric rings
    """
    # total rings
    r = min(rows, cols) // 2
    rings = [[] for _ in range(r)]
    # breakpoint()

    for ring in range(r):
        top = (cols - 1) - 2 * ring
        side = (rows - 1) - 2 * ring
        for i in range(top):
            rings[ring].append(mat[ring][ring + i])
        for j in range(side):
            rings[ring].append(mat[ring + j][ring + top])
        for i in range(top):
            rings[ring].append(mat[ring + side][ring + top - i])
        for j in range(side):
            rings[ring].append(mat[ring + side - j][ring])
    return rings


# rotate individual rings
def rotate_rings(ring, step):
    """
    Rotate the rings anticlockwise by given step
    Parameters
    ----------
    ring: list of integers
    step: integer
    Returns
    -------
    list, rotated anticlockwise by given step
    """
    step %= len(ring)
    res = ring[step:len(ring)]
    res.extend(ring[:step])
    return res


# Put them back in matrix, rows x columns
# TODO
# get the index of element in ring (original)
# put rotated element in those indexes
def put_rings_in_matrix(rings, mat):
    """
    Put rotated rings in Matrix
    Parameters
    ----------
    rings: list of ring
    mat: list, matrix
    Returns
    -------
    list, rows x cols
    """
    r = len(rings)

    for ring in range(r):
        top = (cols - 1) - 2 * ring
        side = (rows - 1) - 2 * ring
        for i in range(top):
            mat[ring][ring + i] = rings[ring].pop(0)
        for j in range(side):
            mat[ring + j][ring + top] = rings[ring].pop(0)
        for i in range(top):
            mat[ring + side][ring + top - i] = rings[ring].pop(0)
        for j in range(side):
            mat[ring + side - j][ring] = rings[ring].pop(0)
    return mat


def rotate_matrix(mat, rows, cols, step):
    rings = concentric_rings(rows, cols, mat)
    rotated_rings = []
    for ring in rings:
        rotated_rings.append(rotate_rings(ring, step))
    res = put_rings_in_matrix(rotated_rings, mat)
    return res


if __name__ == "__main__":
    rows, cols, step = 2, 2, 3
    # mat = matrix(rows, cols)
    mat = [[1, 1], [1, 1]]
    print("Matix:")
    for row in mat:
        print(row)
    print("Rotated Matrix:")
    res = rotate_matrix(mat, rows, cols, step)
    for row in res:
        print(row)

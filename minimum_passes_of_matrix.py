
# Time: O(m * h) | Space: O(m * h) -- where m is the width of the matrix and h is the height of the matrix

def minimumPassesOfMatrix(matrix):
    explore = []
    # append positive values to explore
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                explore.append([row, col])
    steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # Count starts at -1 because we have one final pass for the last numbers we just converted positive
    count = -1
    while explore:
        # This for loop represents one pass through the matrix... 
        # hence the count is incremented once the loop is finished
        for _ in range(len(explore)):
            row, col = explore.pop(0)
            for step in steps:
                adjRow, adjCol = row + step[0], col + step[1]
                if inBoundsAndNegative(adjRow, adjCol, matrix):
                    matrix[adjRow][adjCol] *= -1
                    explore.append((adjRow, adjCol))
        count += 1
    # if explore is empty and all elements are positive, return count
    # if explore is empty and there is still a negative element, we return -1
    return count if checkPositive(matrix) else -1

def checkPositive(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] < 0:
                return False
    return True

def inBoundsAndNegative(row, col, matrix):
    rowInBounds = row >= 0 and row < len(matrix)
    colInBounds = col >= 0 and col < len(matrix[0])
    return rowInBounds and colInBounds and matrix[row][col] < 0
    
            

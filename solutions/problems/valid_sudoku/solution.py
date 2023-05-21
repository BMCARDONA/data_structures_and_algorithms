class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # if a key is not found in the dictionary, the defaultdict will automatically
        # create a new entry for that key with an empty set as its value
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set) 
        big_squares = collections.defaultdict(set) # key = (r // 3, c // 3)
        for r in range(9):
            for c in range(9):
                current_num = board[r][c]
                if current_num == ".":
                    continue
                if current_num in rows[r] or current_num in cols[c] or current_num in big_squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(current_num)
                cols[c].add(current_num)
                big_squares[(r // 3, c // 3)].add(current_num)
        return True
                
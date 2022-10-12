# Time: O(n) | Space: O(n)

def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array) - 1)
    
def minHeightBstHelper(array, left, right):
    if right < left:
        return None
    midIdx = (left + right) // 2
    node = BST(array[midIdx])
    node.left = minHeightBstHelper(array, left, midIdx - 1)
    node.right = minHeightBstHelper(array, midIdx + 1, right)
    return node



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:                
                self.right.insert(value)
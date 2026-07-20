# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findPath(
            node: TreeNode | None,
            target: TreeNode
        ) -> list[TreeNode] | None:
            curr = node
            path = []
            while curr:
                if node is None:
                    return None

                path.append(curr)

                if curr.val == target.val:
                    return path
                elif curr.val > target.val:
                    curr = curr.left
                else:
                    curr = curr.right
        def lowest_common_by_index(list1, list2):
            # 1. Map each item in list2 to its first index position
            # Dictionary lookup takes O(1) time
            indices_list2 = {item: i for i, item in enumerate(list2)}
            
            best_match = None
            min_index_sum = float('inf')
            
            # 2. Loop through list1 and check for matches
            for i, item in enumerate(list1):
                if item in indices_list2:
                    # Combined index score (lower is better)
                    current_sum = i + indices_list2[item]
                    
                    # If this is the lowest index sum we've seen, save it
                    if current_sum < min_index_sum:
                        min_index_sum = current_sum
                        best_match = item
                        
            return best_match

        
        path_to_p = findPath(root, p)
        path_to_q = findPath(root, q)

        return lowest_common_by_index(path_to_p[::-1], path_to_q[::-1])


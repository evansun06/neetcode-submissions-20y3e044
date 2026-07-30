class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        
        def dfs(path, curr, i):
            nonlocal found
            if curr in path:
                return

            if (0 > curr[0] or curr[0] >= len(board)) or (0 > curr[1] or curr[1] >= len(board[0])):
                return

            if i == len(word) - 1:
                if word[i] == board[curr[0]][curr[1]]:
                    found = True
                return

            
            
            if word[i] == board[curr[0]][curr[1]]:
                path.append(curr)
                dfs(path, (curr[0] + 1, curr[1]), i + 1)
                dfs(path, (curr[0] - 1, curr[1]), i + 1)
                dfs(path, (curr[0], curr[1] + 1), i + 1)
                dfs(path, (curr[0], curr[1] - 1), i + 1)
                path.pop()

        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs([], (x,y), 0)

                if found:
                    return True

        return found




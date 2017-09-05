class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False

        visited = [[False for j in len(board[0]) for i in len(board)]]

        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if self.execRecu(board, word, 0, i, j, visited):
                    return True

        return False

    def execRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            visited[i][j] = False

        visited[i][j] = True
        result = self.execRecu(board, word, cur + 1, i - 1, j, visited) or \
                 self.execRecu(board, word, cur + 1, i + 1, j, visited) or \
                 self.execRecu(board, word, cur + 1, i, j - 1, visited) or \
                 self.execRecu(board, word, cur + 1, i, j + 1, visited)
        visited[i][j] = True

        return result
'''
https://leetcode.com/problems/valid-sudoku/
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        

        # check each row
        for rows in board:
            container = []
            for i in rows:
                if i == '.':
                    continue
                if i in container:
                    return False

                else:
                    container.append(i)
        
        # check each column
        for i in range(len(board)):
            container = []
            for column in board:
                if column[i] == '.':
                    continue
                if column[i] in container:
                    return False
                else:
                    container.append(column[i])
            
        # check each box
        d = 0 # took too long to implement - never again
        container = []
        for i in range(3):
            for j in range(9):
                for f in range(d*3,(d*3)+3): # delimit rows to 3
                    if board[j][f] == '.':
                        continue
                    if board[j][f] in container:
                        return False
                    else:
                        container.append(board[j][f])
                if j == 2 or j == 5 or j == 8: # delimit column to 3
                    container = []
            if d >= 2:
                return True
            else:
                d+=1

            

        return True
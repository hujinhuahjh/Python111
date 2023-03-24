def validate_sudoku(board):
    if 0 in board:
        return False
    r,r1,r2 = [],[],[]
    i = 0
    while i < 9:
        for j in range(9):
            r = board[j]
            for n in range(1, 10):
                if n not in r:
                    return False
            r1.append(r[i])
            
        for k in range(9):
            if k+1 not in r1:
                return False 
        r1 = []
        i += 1
        
    i = 0
    while i < 9:
        for j in range(0, 9):
            r = board[j]
            r2.append(r[i])
            r2.append(r[i+1])
            r2.append(r[i+2])
            if j % 3 == 2:
                for a in range(9):
                    if a+1 not in r2:
                        return False 
                r2 = []
        i += 3
    return True
    
print(validate_sudoku([[1,3,2,5,7,9,4,6,8],
				  [4,9,8,2,6,1,3,7,5],
				  [7,5,6,3,8,4,2,1,9],
				  [6,4,3,1,5,8,7,9,2],
				  [5,2,1,7,9,3,8,4,6],
				  [9,8,7,4,2,6,5,3,1],
				  [2,1,4,9,3,5,6,8,7],
				  [3,6,5,8,1,7,9,2,4],
				  [8,7,9,6,4,2,1,5,3]]))

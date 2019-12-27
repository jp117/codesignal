'''
https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr


'''

def matrixElementsSum(matrix):
    length = len(matrix[0])
    new = [[], [], [], [], []]
    output = 0
    
    i = 0
    for i in range(length):
        x = 0
        for x in range(len(matrix)):
            new[i].append(matrix[x][i])
    
    i = 0
    for i in range(length):
        x = 0
        for x in range(len(new[0])):
            if new[i][x] != 0:
                output += new[i][x]
                x += 1
            else:
                break
    return output
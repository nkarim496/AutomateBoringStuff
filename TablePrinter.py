#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[0])):
            if colWidths[i] < len(table[i][j]):
                colWidths[i] = len(table[i][j])   
    for j in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][j].rjust(colWidths[i] + 1), end='')
        print()

printTable(tableData)

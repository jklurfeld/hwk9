def calculate_knapsack(items, values, weights, max_weight):
    #This is a recurisve helper function to return the knapsack.
    def knapsack(i: int, j: int):
        if i == 0:
            return {}
        if cell[i][j] > cell[i-1][j]:
            return {items[i-1]}.union(knapsack(i-1,j-weights[i-1]))
        else:
            return knapsack(i-1,j) 
        
    # Start of calculate_knapsack code:    
    # We are going to add a zero items (row) and zero weights (column)
    #   because Python lists allow for negative indexing.
    #   It also makes the problem slightly easier to solve.
    row_len = len(items) + 1
    col_len = max_weight + 1
    cell = []
    for i in range(row_len):
        row = [0] * col_len
        cell.append(row)
    
    #Note: The zero row/column already has zeros in it.
    for i in range(1, row_len):
        item_num = i - 1
        for w in range(1, col_len):
            if weights[item_num] > w:
                cell[i][w] = cell[i-1][w]
            else:
                cell[i][w] = max(cell[i-1][w], cell[i - 1][w - weights[item_num]] + values[item_num])
    
    # #This is the maximum value you can store in the knapsack.
    print(cell[row_len-1][col_len-1])
    # #Let's check our answer.
    for i in range(len(cell)):
        print(cell[i])

    return knapsack(row_len-1, col_len-1)
    
def main():
#   #wikisac
#   items   = ['A','B','C','D']
#   values  = [5,4,3,2]
#   weights = [4,3,2,1]
#   capacity = 6
#   #textbook1
#   items   = ['Guitar','Stereo','Laptop']
#   values  = [1500,3000,2000]
#   weights = [1,4,3]
#   capacity = 4
#   #textbook2
#   items   = ['Guitar','Stereo','Laptop','iPhone']
#   values  = [1500,3000,2000,2000]
#   weights = [1,4,3,1]
#   capacity = 4
  items   = ['Pillow','Glasses Case','Windscreen','Sandals','Swimsuit-Towel']
  values  = [5,3,1,2,2]
  weights = [3,1,1,2,3]
  capacity = 6
  print(calculate_knapsack(items, values, weights, capacity))
main()
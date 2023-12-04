from random import randint

### Part 1: Lumber Mill
def lumberSelection(prices:list, n:int) -> float:
    #This is a recurisve helper function to return the knapsack.
    # def knapsack(i: int, j: int):
    #     if i == 0:
    #         return {}
    #     if cell[i][j] > cell[i-1][j]:
    #         return {boards[i-1]}.union(knapsack(i-1,j-i-1))
    #     else:
    #         return knapsack(i-1,j) 
        
    # Start of calculate_knapsack code:    
    # We are going to add a zero items (row) and zero weights (column)
    #   because Python lists allow for negative indexing.
    #   It also makes the problem slightly easier to solve.
    row_len = n + 1
    col_len = n + 1
    cell = []
    for i in range(row_len):
        row = [0] * col_len
        cell.append(row)
    
    #Note: The zero row/column already has zeros in it.
    for i in range(1, row_len):
        # item_num is the length?
        for w in range(1, col_len):
            if i > w:
                cell[i][w] = cell[i-1][w]
            else:
                cell[i][w] = max(cell[i-1][w], cell[i - 1][w - i] + prices[i-1])
    
    # #This is the maximum value you can store in the knapsack.
    # print(cell[row_len-1][col_len-1])
    # #Let's check our answer.
    for i in range(len(cell)):
        print(cell[i])

    # return cell[n][n]
    return cell[row_len-1][col_len-1]

    # return knapsack(row_len-1, col_len-1)

### Part 2: Cash Register
def getNumberOfWays(change_amount:int, bill_list:list) -> int:

    row_len = len(bill_list) + 1
    col_len = change_amount + 1
    cell = []

    for i in range(row_len):
        row = [0] * col_len
        cell.append(row)

    for i in range(1, col_len):
        cell[1][i] = 1

    for bill_num in range(2, row_len):
        for change in range(1, col_len):
            bill = bill_list[bill_num-1]

            # give the cell the value of the cell above it
            cell[bill_num][change] = cell[bill_num -1][change]
            if bill <= change:
                cell[bill_num][change] += cell[bill_num][change-bill] 

    #Let's check our answer.
    for i in range(len(cell)):
        print(cell[i])

    # return cell[n][n]
    return cell[row_len-1][col_len-1]


def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size =6 #randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = 12
    print("For $" + str(change) + " there are " + str(getNumberOfWays(change, bills)) + " combinations.")

if __name__ == '__main__': 
    main()
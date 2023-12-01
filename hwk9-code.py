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
    row_len = len(prices) + 1
    col_len = n + 1
    cell = []
    for i in range(row_len):
        row = [0] * col_len
        cell.append(row)
    
    #Note: The zero row/column already has zeros in it.
    for i in range(1, row_len):
        item_num = i - 1
        # item_num is the length?
        for w in range(1, col_len):
            if item_num > w:
                cell[i][w] = cell[i-1][w]
            else:
                cell[i][w] = max(cell[i-1][w], cell[i - 1][w - item_num] + prices[item_num])
    
    # #This is the maximum value you can store in the knapsack.
    # print(cell[row_len-1][col_len-1])
    # #Let's check our answer.
    for i in range(len(cell)):
        print(cell[i])

    # return cell[n][n]
    return cell[row_len-1][col_len-2]

    # return knapsack(row_len-1, col_len-1)

### Part 2: Cash Register
def getNumberOfWays(change_amount:int, bill_list:list) -> int:
	return 0

def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = 2 #randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(6, bills)) + " combinations.")

if __name__ == '__main__': 
    main()


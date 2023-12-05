# Names: Jessica Klurfeld and Michelle Lawson
# Peers: N/A
# References: algorithms adapted from Knapsack.py from in-class

from random import randint

### Part 1: Lumber Mill
def lumberSelection(prices:list, n:int) -> float:
    #Initialize 2D array with 0s 
    row_len = n + 1
    col_len = n + 1
    cell = []
    for i in range(row_len):
        row = [0] * col_len
        cell.append(row)
    
    #Note: The zero row/column already has zeros in it.
    for i in range(1, row_len):
        for w in range(1, col_len):

            if i > w: # if the length of the lumber is greater than the length of the board
                # give the cell the value of the cell above it
                cell[i][w] = cell[i-1][w]
            else:
                # give the cell the max value of the cell above it and the cell at the remaining length
                cell[i][w] = max(cell[i-1][w], cell[i][w-i] + prices[i-1])

    return cell[row_len-1][col_len-1]


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

            if bill <= change: # if bill can fit into the change

                # add 1 more combination if the change is equal to the bill
                if change - bill == 0:
                    cell[bill_num][change] += 1

                # else add the remaining combinations not accounted for by the cell above it
                else:
                    cell[bill_num][change] += cell[bill_num][change-bill] 

    # return cell[n][n]
    return cell[row_len-1][col_len-1]


def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(change, bills)) + " combinations.")

if __name__ == '__main__': 
    main()
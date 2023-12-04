def getNumberOfWays(change_amount: int, bill_list: list) -> int:
    def countWays(change, bills, memo):
        if change == 0:
            return 1
        if change < 0 or bills == 0:
            return 0
        if memo[bills][change] != 0:
            return memo[bills][change]

        # Including the last bill
        count1 = countWays(change - bill_list[bills - 1], bills, memo)

        # Excluding the last bill
        count2 = countWays(change, bills - 1, memo)

        memo[bills][change] = count1 + count2
        return memo[bills][change]

    # Initialize memoization table with -1
    memo = [[0 for _ in range(change_amount + 1)] for _ in range(len(bill_list) + 1)]

    # Count ways and fill the table
    countWays(change_amount, len(bill_list), memo)

    # Print the table
    for row in memo:
        print(row)

    return memo[len(bill_list)][change_amount]

def find_combinations(change_amount, bill_list):
    def find_ways(amount, bills, current_combination, all_combinations):
        if amount == 0:
            all_combinations.append(list(current_combination))
            return
        if amount < 0 or not bills:
            return

        # Include the last bill in the combination
        current_combination.append(bills[-1])
        find_ways(amount - bills[-1], bills, current_combination, all_combinations)

        # Exclude the last bill from the combination
        current_combination.pop()
        find_ways(amount, bills[:-1], current_combination, all_combinations)

    all_combinations = []
    find_ways(change_amount, bill_list, [], all_combinations)
    return all_combinations



def main():
    bill_list = [1, 2, 5, 10]
    change_amount = 11
    print(getNumberOfWays(change_amount, bill_list))


    # Change amount and bill list
    change_amount = 8
    bill_list = [1, 2, 5]

    # Find all combinations
    combinations = find_combinations(change_amount, bill_list)
    combinations.sort()
    combinations

main()

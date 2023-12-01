# dictionary with the prices for the different lengths of a board
length_prices = {
    1: 0.25,
    2: 1.45,
    4: 3.58,
    6: 4.40,
    8: 5.18,
    10: 6.58,
    12: 8.28
}


# calculate different combinations of boards given one length, while order does not matter
def calculate_combinations(length):
    # create a list of all possible combinations
    combinations = []
    
    # recursive function to calculate all combinations
    def calculate(length, combination):
        # if the length is 0, add the combination to the list
        if length == 0:
            combinations.append(combination)
        # if the length is not 0, calculate all possible combinations
        else:
            # loop through all possible lengths
            for i in length_prices:
                # if the length is smaller than the current length, calculate the combinations
                if i <= length:
                    calculate(length - i, {**combination, **{i: combination.get(i, 0) + 1}})

    # call the recursive function
    calculate(length, {})

    # delete all duplicates
    combinations = [dict(t) for t in {tuple(d.items()) for d in combinations}]
    

    # return the list of combinations
    return combinations


def main():
    print(calculate_combinations(12))

main()



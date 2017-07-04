# Example:
# Given [1,2,2,4,5], add each value together except
# where there are values that are matching. In this
# case, try adding 1 to one of the matching values
# to create a new unique value and add that to the
# running total.
# Eg: One of the 2s becomes a three and the list
# becomes [1,2,3,4,5] with a total sum of 15.


def lowest_summation_of_unique_values(arr):
    total = 0
    seen = set()

    for n in arr:
        if n not in seen:
            seen.add(n)
            total += n
        elif n in seen:
            while n in seen:
                n = n+1
            seen.add(n) # This line can be removed if we don't care about n+1 being added to our list of unique values.
            total += n
    return total
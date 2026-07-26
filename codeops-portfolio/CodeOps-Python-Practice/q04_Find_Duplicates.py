from collections import Counter


def find_duplicates(numbers: list[int]) -> list[int]:
    
    #Return all duplicate values in the list.

    counts = Counter(numbers)
    return [number for number, frequency in counts.items() if frequency > 1]


# Example
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
print(find_duplicates([5, 5, 5]))
print(find_duplicates([1, 2, 3]))
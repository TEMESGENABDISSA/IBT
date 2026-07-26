from collections import defaultdict

def group_anagrams(words):
    """
    Groups words that are anagrams.

    Time Complexity: O(n * k log k)
    Space Complexity: O(n * k)
    """

    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# Example
print(group_anagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat"]
))
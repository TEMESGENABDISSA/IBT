def longest_unique(s):
    
    #Returns length of longest substring
   # without repeating characters.
    

    char_index = {}

    left = 0

    longest = 0


    for right, char in enumerate(s):

        # Character already exists in current window
        if char in char_index and char_index[char] >= left:

            left = char_index[char] + 1


        char_index[char] = right


        current_length = right - left + 1


        longest = max(
            longest,
            current_length
        )


    return longest



# Testing

print(
    longest_unique("abcabcbb")
)

print(
    longest_unique("bbbbb")
)

print(
    longest_unique("pwwkew")
)

print(
    longest_unique("")
)
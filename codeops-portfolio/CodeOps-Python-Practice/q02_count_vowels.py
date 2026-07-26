def count_vowels(word):
    vowels = "aeiou"
    word = word.lower()
    count = 0

    for letter in word:
        if letter in vowels:
            count += 1

    return count

# Test the function
txt = "temesgen"
result = count_vowels(txt)

print(f"Your word is: {txt}")
print(f"Counted vowels in the word: {result}")
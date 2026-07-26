from collections import Counter
import string


def word_frequency(text: str) -> dict[str, int]:
    
    #Count the frequency of every word.
    
    translator = str.maketrans("", "", string.punctuation)
    cleaned = text.lower().translate(translator)
    return dict(Counter(cleaned.split()))


# Example
text = "Hello world hello, Python world!"

print(word_frequency(text))
# First import the Counter library

from collections import Counter


# Read the text file -->

with open("scrap.txt", "r",encoding="utf-8") as f:
    content = f.read()

# Split the text into words and create a counter object to count the word frequencies -->
 
words = content.split()

word_counts = Counter(words)

# Print the words and their frequencies

print("Words and their frequencies :")
for word, frequency in word_counts.most_common():
    print(f"{word}: {frequency}")

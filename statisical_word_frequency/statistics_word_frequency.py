import nltk
import csv
from nltk.tokenize import word_tokenize

nltk.download('punkt')


filePath = "/Users/beishan/Documents/The Martain (Weir Andy) (Z-Library).txt"

with open(filePath, encoding="utf-8") as f:
    book_content = f.read()

words = word_tokenize(book_content)
word_frequency = {}

for word in words:
    word = word.lower()
    if word.isalpha() and len(word) > 3:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

with open("word_frequency.csv", "w", newline='') as f:
    csv_writer = csv.writer(f)

    for word in sorted_word_frequency.items():
        print(f'{word}')
        csv_writer.writerow(word)


print(f'Words: {len(sorted_word_frequency.keys())}')
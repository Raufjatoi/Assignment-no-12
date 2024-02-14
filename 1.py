# 1. Word Counter:
#  Write a program that reads a sentence and counts the number of times each word appears. Use 
# a dictionary to store the word counts
def count_words(sentence):
    word_counts = {}  
    words = sentence.split()
    
    for word in words: 
        word = word.strip('.,!?;:"\'').lower()
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

sentence = input("Enter a sentence: ")
word_counts = count_words(sentence)

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

    

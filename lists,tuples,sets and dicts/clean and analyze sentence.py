sentence = input()
position = int(input())

#to remove outer space and convert to lower case
clean = sentence.strip().lower()

#replace punctuations with space
punctuations = ".,,,!,?,;,:,"
for ch in punctuations:
    clean = clean.replace(ch," ")

#split the sentences into words and rebuild cleaned sentence
split_sent = clean.split()
final_sent = " ".join(split_sent)
#extract the required words and slices
first_word = split_sent[0]
last_word = split_sent[-1]

required = split_sent[position-1]
first_word_prefix = clean[0:3]
last_word_suffix = clean[-4: ]

print(f"Cleaned Sentence: {final_sent}")
print(f"Word Count: {len(split_sent)}")
print(f"First Word: {first_word}")
print(f"Last Word: {last_word}")
print(f"Selected Word: {required}")
print(f"First word prefix: {first_word_prefix}")
print(f"Last word suffix: {last_word_suffix}")






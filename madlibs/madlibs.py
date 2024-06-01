

with open(r"code_projects\madlibs.txt", "r") as file:
    story = file.read()

words = []
start_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_word = i
    
    if char == target_end and start_word != -1:
        word= story[start_word: i +1]
        words.append(word)
        start_word = -1

answer = {}

for word in words:
    response = input(f"Enter a word for {word}:")
    answer[word] = response

print(answer)

for word in words:
    story = story.replace(word, answer[word])

print(story)

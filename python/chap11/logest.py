filename = input("파일명을 입력하세요: ").strip()
infile = open(filename, "r")

max_length = 0
for line in infile:
    for word in line.split():
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
print(word)
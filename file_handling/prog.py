f = open("file_handling/ayush_result.txt", "r")
data = f.read()
words = data.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("longest word ",longest)
f.close()
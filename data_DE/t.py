import json

a = []
for line in open("words_de.txt").readlines():
    a.append(line)

try:
    json.dump(a, open("words.json", "w"))
except FileNotFoundError:
    json.dump(a, open("words.json", "x"))

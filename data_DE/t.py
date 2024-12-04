import json

a = []
for line in open("words_de.txt", encoding="utf-8").read().split("\n"):
    line = str(line)
    line = line.replace("\u00e4", "ä")
    line = line.replace("\u00fc", "ü")
    line = line.replace("\u00f6", "ö")
    a.append(line)

try:
    json.dump(a, open("words.json", "w"))
except FileNotFoundError:
    json.dump(a, open("words.json", "x"))

words = input("> ").split(" ")
d = {
    ":)" : "🙂",
    ":(" : "😞"
}
op = ""
for word in words:
    if word in d.keys():
        op += d.get(word) + " "
        continue
    op += word + " "
print(op)
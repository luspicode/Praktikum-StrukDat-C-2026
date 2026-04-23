web = []

# Push
web.append('youtube.com')
web.append('w3schools.com')
web.append('chatgpt.com')
print("Stack: ", web)

# isEmpty
isEmpty = not bool(web)
print("isEmpty: ", isEmpty)

# Pop
poppedElement = web.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", web)

# Peek
topElement = web[-1]
print("Peek: ", topElement)

# Size
print("Size: ",len(web))
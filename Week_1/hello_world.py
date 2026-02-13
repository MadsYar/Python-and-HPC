text = "Hello world"

with open('content.txt', 'w') as file:
    file.write(text)

print(text)
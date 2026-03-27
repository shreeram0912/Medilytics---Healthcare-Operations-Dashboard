file = open("hi.py", "w")
file.write(print("Hello, world!"))
file.close()

file = open("hi.py", "r")
content = file.read()
file.close()

print(content)
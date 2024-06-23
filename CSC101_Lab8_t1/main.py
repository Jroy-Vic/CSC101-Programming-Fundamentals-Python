filename = "hello.txt"
filename2 = "nope.txt"
lines = ["hello\n", "world\n", "star wars"]
with open(filename, "r+") as some_file:
    contents = some_file.read()
    print(contents)
    some_file.writelines(lines)

try:
    with open(filename2, "r") as some_file:
        contents = some_file.read()
        print(contents)
except FileNotFoundError:
    print("No file!")

user_input = input("Enter something to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

extra_input = input("Enter something more to append: ")
with open("output.txt", "a") as file:
    file.write(extra_input + "\n")

print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    print(file.read())

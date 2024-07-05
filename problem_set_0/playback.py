#Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

user_input = input("Write something with withe spaces: ")
replace_dot = user_input.replace(" ","...")
print(f"Read with slower pace: {replace_dot}")
""" Implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
Punctuation and whitespace should be outputted unchanged. 
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input."""

user_input = input("Just write something: ")
user_input_in_lower = user_input.lower()
print(f"This is how it look like in lower case :{user_input_in_lower}.")
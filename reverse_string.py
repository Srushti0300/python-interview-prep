# Problem: Reverse a string without using slicing
# Example: Input "hello" -> Output "olleh"

def reverse_string(s):
    reversed_str = ""              # empty string to build result
    for char in s:                 # loop through each character in s
        reversed_str = char + reversed_str   # add new char to the FRONT
    return reversed_str

print(reverse_string("Dad"))
solutions _<5240100788>_2025.py

"""
Solutions to assignment 3
"""
"""
1. Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Solution 1
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)  # Output: gnimmargorP


"""
2. Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Solution 2
full_name = input("Enter your full name: ")
initials = '.'.join([name[0].upper() for name in full_name.split()])
print(initials)  # Example Output: J.D.


"""
3. Write a Python program to check if a given string is a palindrome. 
A palindrome reads the same forwards and backward (e.g., "radar", "level"). 
Hint: Compare the string with its reverse.
"""
# Solution 3
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
4. Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Solution 4
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Number of words: {word_count}")


"""
5. Write a Python program to replace all occurrences of "is" with "was" in the string 
"This is a string and it is an example." Print the modified string.
"""
# Solution 5
original_text = "This is a string and it is an example."
modified_text = original_text.replace("is", "was")
print(modified_text)  # Output: Thwas was a string and it was an example.
"""

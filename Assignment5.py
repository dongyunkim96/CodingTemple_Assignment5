# Solution (Even or Odd)
def even_or_odd(number):
    # If the number is divisible by 2, return "Even"; otherwise, return "Odd"
    return "Even" if number % 2 == 0 else "Odd"

# Solution (Convert a Number to a String)
def number_to_string(num):
    return str(num)  # str() converts any value to its string representation

# Solution (Remove String Spaces)
def no_space(x):
    # Replace all spaces in the string with an empty string
    return x.replace(" ", "")

# Solution (Vowel Count)
def count_vowels(sentence):
    # Define the set of vowels
    vowels = "aeiou"
    # Use a generator expression to count characters in the string that are vowels
    return sum(1 for char in sentence if char in vowels)
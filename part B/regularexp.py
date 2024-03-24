# This script demonstrates the use of regular expressions in Python
# The 're' module provides the functionality for working with regular expressions
import re

# This string will be used for the regular expression operations
text = "Hello, I have 10 apples and 5 oranges. Apples are tasty!"

# re.match(pattern, string) tries to match the pattern at the beginning of the string
if re.match(r"^Hello", text):
    print("Match found at the beginning of the text")
else:
    print("No match found at the beginning of the text")

# re.search(pattern, string) tries to find the first occurrence of the pattern anywhere in the string
match = re.search(r"\d+", text)  # \d matches any digit
if match:
    print("First digit found:", match.group())  # match.group() returns the matched pattern

# re.findall(pattern, string) finds all occurrences of the pattern in the string
digits = re.findall(r"\d+", text)
print("All digits found:", digits)

# re.sub(pattern, repl, string, count=0, flags=0) substitutes occurrences of the pattern with the replacement string
new_text = re.sub(r"apples", "bananas", text)  # count=0 replaces all occurrences
print("Modified text:", new_text)

# re.split(pattern, string, maxsplit=0) splits the string using the pattern as the delimiter
words = re.split(r"\W+", text)  # \W matches any non-word character (i.e. non-alphanumeric)
print("Split words:", words)


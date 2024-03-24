import re

text = "Hello, I have 10 apples and 5 oranges. Apples are tasty!"

if re.match(r"^Hello", text):
    print("Match found at the beginning of the text")
else:
    print("No match found at the beginning of the text")

match = re.search(r"\d+", text)
if match:
    print("First digit found:", match.group())

digits = re.findall(r"\d+", text)
print("All digits found:", digits)

new_text = re.sub(r"apples", "bananas", text)
print("Modified text:", new_text)

words = re.split(r"\W+", text)
print("Split words:", words)

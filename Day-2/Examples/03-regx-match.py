import re

text = "The quick brown fox"
pattern = "quick"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
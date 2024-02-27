#map
text = "hello world"
capitalized_text = ''.join(map(lambda x: x.upper(), text))
print(capitalized_text)  # Output: "HELLO WORLD"


#reduce
from functools import reduce
text = ["h","e","l","l","o"]
concatenated_text = reduce(lambda x, y: x + y, text)
print(concatenated_text)  # Output: "hello"


#filter
text = "hello world"
filtered_text = ''.join(filter(lambda x: x in 'aeiou', text))
print(filtered_text)  # Output: "eoo"

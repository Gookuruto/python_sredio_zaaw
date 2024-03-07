import re

text = "Kontaktuj się ze mną pod adresem john.doe@example.com lub jane@example.org."
pattern = r"[a-zA-Z0-9.+-_]{2,}@[a-zA-Z0-9]{1,3}.[a-zA-Z0-9]*\.?[a-z]{0,10}"
list = re.findall(pattern, text)
print(list)
import re

text = "Kontaktuj się ze mną pod adresem john.doe@example.com lub jane@example.org."
pattern = r"[a-zA-Z0-9.+-_]{2,}@[a-zA-Z0-9]+\.[a-zA-Z0-9+\.{1}]?[a-z]{0,10}"
list = re.findall(pattern, text)
# () -> robi grupy ktore find bedzie zawsze probowal dopasowac
# {} -> zawiaraja informacje ile razy poprzedzajacy element moze sie powtorzyć
# [] -> grupuja warunki wewnatrz i mozna do nich uzywac specjalnych modyfikatorow np. [a-z]?
for match in list:
    print(match)


text = "Numer telefonu: 123-456-7890, drugi numer: 987-654-3210"

pattern = r"(\d{3})-(\d{3})-(\d{4})"

matches = re.findall(pattern,text)
for i in matches:
    area_code, first_part, second_part = i
    print("Kod Obszaru:", area_code)
    print("Pierwsza czesc", first_part)
    print("Druga czesc", second_part)
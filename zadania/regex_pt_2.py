'''
Wyszukiwanie adresów email:
Znajdź wszystkie adresy email w pliku tekstowym.

Wyszukiwanie numerów telefonów:
Zidentyfikuj i wyodrębnij wszystkie numery telefonów, które występują w różnych formatach (np. (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890, +48 123-456-789).

Wyszukiwanie dat:
Znajdź wszystkie daty w pliku tekstowym (np. DD-MM-YYYY, DD/MM/YYYY, YYYY-MM-DD).

Wyszukiwanie adresów IP:
Zidentyfikuj i wyodrębnij wszystkie adresy IP (zarówno IPv4, jak i IPv6) występujące w tekście.

Wyszukiwanie kodów pocztowych:
Znajdź i wyodrębnij wszystkie kody pocztowe w formacie używanym w określonym kraju.

Wyszukiwanie URL-i:
Zidentyfikuj wszystkie adresy URL (zarówno HTTP, HTTPS, FTP, jak i inne protokoły) w tekście.

Wyszukiwanie numerów ID:
Znajdź wszystkie numery identyfikacyjne (np. numery ID klientów, numer PESEL, numery identyfikacyjne produktów) w tekście.

Wyszukiwanie hashtagów:
Zidentyfikuj i wyodrębnij wszystkie hashtagi (rozpoczynające się od znaku #) używane w tekście.

Wyszukiwanie adresów URL obrazków:
Znajdź wszystkie adresy URL obrazków (np. .jpg, .png, .gif) w tekście.

Wyszukiwanie nazw użytkowników:
Zidentyfikuj wszystkie nazwy użytkowników (np. w formacie @username) używane w mediach społecznościowych lub innych platformach komunikacyjnych.
'''



#email

import re

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin aliquam mauris eget leo lacinia, email@example.com. Integer vitae tempor mauris. Ut pulvinar urna et lorem pharetra, john.doe@email.com. Duis sit amet tellus eu tellus luctus rhoncus. Nam maximus lacus et velit eleifend, lorem@ipsum.com."

emails = re.findall('', text)
print(emails)


#tel-numbers
import re

text = "Kontakt: 123-456-7890, +48 123 456 789, (987) 654-3210, 0123456789"

phones = re.findall('', text)
print(phones)

#daty
import re

text = "Data transakcji: 2023-12-25, 12/25/2023, 25.12.2023"

dates = re.findall('', text)
print(dates)

#adresy ip
import re

text = "Adresy IP: 192.168.1.1, 10.0.0.1, 2001:0db8:85a3:0000:0000:8a2e:0370:7334"

ips = re.findall('', text)
print(ips)

#kody pocztowe

import re

text = "Kody pocztowe: 12345, 12-345, 12 345, 12-3456, 12345-6789"

zip_codes = re.findall('', text)
print(zip_codes)

#urls
import re

text = "Więcej informacji na stronie https://www.example.com lub na naszym forum: http://forum.example.com"

urls = re.findall("", text)
print(urls)

#user id

import re

text = "ID użytkownika: 123456789, Numer klienta: K123-456-789, Numer PESEL: 12345678901"

ids = re.findall('', text)
print(ids)


#hashtags
import re

text = "Temat dnia: #Python, #MachineLearning, #DataScience"

hashtags = re.findall('', text)
print(hashtags)

#images

import re

text = 'Obrazki: <img src="http://example.com/image1.jpg">, <img src="https://example.com/image2.png">'

img_urls = re.findall('', text)
print(img_urls)

#usernames
import re

text = "Znajdź nas na Twitterze: @username1, @username2, @username3"

usernames = re.findall('', text)
print(usernames)








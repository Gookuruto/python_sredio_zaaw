#1
r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#2
r'\b(?:\+\d{1,2}\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
#3
r'\b\d{2}[./-]\d{2}[./-]\d{4}\b'
#4
r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}\b'
#5
r'\b\d{5}(?:-\d{4})?\b|\b\d{2}[-\s]?\d{3}\b'
#6
r'\bhttps?://\S+\b'
#7
r'\b(?:[A-Z]?\d{3}[- ]?\d{3}[- ]?\d{3}|[A-Z]?\d{9})\b'
#8
r'#\w+'
#9
r'<img\s+src="([^"]+\.(?:jpg|png|gif))"'
#10
r'@\w+'

text = text.lower()

count = 0
for ch in text:
    if ch.isalpha() and ch not in "aeiou":
        count += 1
return count
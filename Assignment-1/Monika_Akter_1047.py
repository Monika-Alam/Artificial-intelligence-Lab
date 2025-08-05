full_name = input("Enter your full name: ")

# 1. Count vowels and consonants
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel_count = 0
consonant_count = 0

for ch in full_name:
    for v in vowels:
        if ch == v:
            vowel_count += 1
    for c in consonants:
        if ch == c:
            consonant_count += 1

# 2. ASCII values of each character
ascii_values = []
for ch in full_name:
    ascii_values.append(ord(ch))

# 3. Reversed version of the name
reversed_name = ""
for i in range(len(full_name)-1, -1, -1):
    reversed_name += full_name[i]

# 4. Palindrome check
cleaned_name = ""
for ch in full_name:
    if ch != ' ':
        if 'A' <= ch <= 'Z':  # manually convert uppercase to lowercase
            ch = chr(ord(ch) + 32)
        cleaned_name += ch

is_palindrome = True
for i in range(len(cleaned_name)//2):
    if cleaned_name[i] != cleaned_name[len(cleaned_name)-1-i]:
        is_palindrome = False
        break

# 5. Unique letters finding
unique_letters = []
for ch in full_name:
    if ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
        found = False
        for u in unique_letters:
            if ch == u:
                found = True
                break
        if not found:
            unique_letters.append(ch)

n = len(unique_letters)
for i in range(n):
    for j in range(0, n-i-1):
        if ord(unique_letters[j]) > ord(unique_letters[j+1]):
            temp = unique_letters[j]
            unique_letters[j] = unique_letters[j+1]
            unique_letters[j+1] = temp

# 6. unique character
first_non_repeating = None
for ch in full_name:
    if ch != ' ':
        count = 0
        for ch2 in full_name:
            if ch == ch2:
                count += 1
        if count == 1:
            first_non_repeating = ch
            break

#  Output
print("Full Name:", full_name)
print("Vowels:", vowel_count, ", Consonants:", consonant_count)
print("ASCII Values:", ascii_values)
print("Reversed Name:", reversed_name)
print("Is Palindrome:", is_palindrome)
print("Unique Letters (sorted):", unique_letters)
print("First Non-Repeating Character:", first_non_repeating)

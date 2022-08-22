import cs50

letters = 0
words = 1
sentences = 0
s = cs50.get_string("Text: ").lower()

for i in range(len(s)):
    if (s[i].isalpha()):
        letters += 1
    elif (s[i] == ' ' and s[i + 1]):
        words += 1
    elif (s[i] == '?' or s[i] == '!' or s[i] == '.'):
        sentences += 1

L = float(letters / words * 100)
S = float(sentences / words * 100)
index = round((float)(0.0588 * L - 0.296 * S - 15.8))
if (index >= 16):
    print('Grade 16+')
elif (index < 1):
    print('Before Grade 1')
else:
    print('Grade ', index)

s = input("Enter your name: ")
i = len(s) - 1
s1 = ""
while i >= 0:
    if i == len(s) - 1:
        s1 += s[i].upper()
    else:
        s1 += s[i].lower()
    i -= 1
print(s1)
if s1.lower() == s.lower():
        print("Palindrome!")
else:
        print("not a palindrome")
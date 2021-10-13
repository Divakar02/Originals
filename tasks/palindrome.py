# a=mom
txt=(input("Enter text: ")).lower()
i=len(txt)//2
a=txt[:i]
b=txt[i+1:][::-1]
if a==b:
    print(f"{txt} is a palindrome")
else:
    print(f"{txt} is not palindrome")


x=str(input("Enter the alphabet"))
cons=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowel=['a','e','i','o','u']
if any(cons):
    print(f"{x} is consonant")
if x in (vowel):
    print(f"{x} is vowel")
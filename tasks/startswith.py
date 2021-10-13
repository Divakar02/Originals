x=input("Enter the sentence: ")
y=[x]
para=y[0].split()
let=input("Enter the letter to startwith: ")
for i in para:
    if i.startswith(let):
        print(i)

word=list(input("Enter the word: "))
vowel=['a','e','i','o','u','A','E','I','O','U']
vowel_num=0
cons_num=0
splchar=['!','@','$','%','^','&','*','_']
splcharnum=0
int_num=0
for i in word:
    if i in vowel:
        vowel_num+=1
    if i not in vowel and i not in splchar and i not in list(range(1,10)):
        cons_num+=1
    if i in splchar:
        splcharnum+=1
    if i in list(range(1,10)):
        int_num+=1
print(f'Consontants={cons_num}\n Vowel={vowel_num}\n SplChar={splcharnum}\n Integer={int_num}')






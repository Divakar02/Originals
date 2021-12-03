'''
dict1={"Jaya":21,"A":43,"B":32,"C":12}
dict1={i:("Young" if (j<=30) else "old") for (i,j) in dict1.items()}

a={k:v if 1>2 else k:v for k,v in dict1.items()}
# lst=['a','B','c','D','E']
D={ i:(i.upper() if i.islower() else i.lower()) for i in lst }

# D={i:i**2 for i in [int(input()) for i in range(5)]}'''

dict={}
for i,j in dict.items():
       print(i,j)

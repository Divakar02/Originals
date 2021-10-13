list=[11,45,8,23,14,12,78,45,89]
chunk1=[]
chunk2=[]
chunk3=[]

for i in range(len(list)):
    if i<3:
        chunk1.append(list[i])
    if i>3 and i<7:
        chunk2.append(list[i])
    if i>7:
        chunk3.append(list[i])

print(f'Chunk1 {chunk1}\nAfter reversing it {chunk1[::-1]}')
print(f'Chunk2 {chunk2}\nAfter reversing it {chunk2[::-1]}')
print(f'Chunk2 {chunk3}\nAfter reversing it {chunk3[::-1]}')


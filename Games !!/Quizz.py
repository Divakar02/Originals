import random

dict={'How many notes are there in a musical scale?': '7',
 'What temperature centigrade does water boil at?': '100',
 'What company is also the name of one of the longest rivers in the world?': 'Amazon',
 'What in the animal kingdom is a doe?': 'female deer',
 'What is the tallest mountain in the world?': 'Mount Everest',
 'How many centimetres in a metre': '100',
 'What language is spoken in Norway?': 'Norwegian',
 'What is the busiest airport in Britain called?': 'London Heathrow',
 'Who is next in line to the British throne after Queen Elizabeth II': 'Prince Charles',
 'What number is a baker’s dozen?': '13'}

A=random.choices(list(dict.keys()))
print(*A)

A="".join(A) #converting list to string

answer=input("Enter answer: ")

if dict['What number is a baker’s dozen?']==answer:
    print("Correct")
else:
    print(f"Wrong!! Answer: {dict[A]}")


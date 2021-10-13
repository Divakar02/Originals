name=str(input("Enter your name: "))
s1=int(input("Enter Tamil marks  : "))
s2=int(input("Enter English marks: "))
s3=int(input("Enter Maths marks  : "))
s4=int(input("Enter Science marks: "))
s5=int(input("Enter Social marks : "))
total=s1+s2+s3+s4+s5

avg=total/5
print(f"Total Marks ={total}")
print(f"Average Marks={avg}")

if len(str(s1))>2 or len(str(s1))>2 or len(str(s1))>2 or len(str(s1))>2 or len(str(s1))>2:
    print("Enter valid marks!")
if avg>90:
    print("Excellent! Keep it up.")
if avg>50 and avg<90:
    print("Good !")
if avg<50:
    print("Try Harder!")

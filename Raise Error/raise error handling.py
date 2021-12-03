import csv

file=open('error_data.csv','r')

c=0
for i in csv.reader(file):
    print(i[0],end=' '*(22-len(i[0])))
    c+=1
    if c==5:
        c=1
        print()


error_input=input("\n Enter the error u wanna raise")
display_msg=input("Enter the msg u wanna display: ")

exec(f"raise {error_input}('{display_msg}')")




file.close()




f=open("demo.txt","r+")
reader=f.readlines()

name=input("Enter Name: ").capitalize()
print(name)
password=input("Give your Password: ")

check=None

for i in reader:
    # if i.isalpha() and not i.isnumeric():
    if name in i:
        print("Your username and pass is already present")

        break
    else:
        check='no'


if check=='no':
    f.write(f"\nUser {name}\n")
    f.write(f"Password {password}")
    print("Your name and password was updated succesfully")






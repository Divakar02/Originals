# 0-product
# 1-price
# 2-quantity

print("Welcome to Dairy Store!!\n")

import csv

'''def csv_printer(file):
    for line in csv.reader(open(file)):
        length = ' ' * (8 - len(line[0]))
        print(line[0], line[1], sep=length, end=f' {line[2]}\n')
    print()
#printing bill
csv_printer("Product.csv")
# initializations
bill=0
check=0


# while input("Hit enter to Proceed: ").lower() == "\n":
x=0
while input("Wish to proceed?(Yes/No)\n").lower()!="no":
    product = input("Enter the name of dairy product: ").capitalize()
    with open("Product.csv") as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for lines in csv_file:
            if product == lines[0]:
                print(f'--Item:{product}\n--Price: {lines[1]}\n--Quantity: {lines[2]}')

                qnt=int(input("How much Qnty you need?: "))
                print("Great!")

                bill += (qnt * int(lines[1]))
                with open("Bill.csv",'a',newline='') as bill_file:
                    bill_csv = csv.writer(bill_file)
                    bill_csv.writerow([product,f'{lines[1]}({qnt})',(qnt*int(lines[1]))])
                check=1
    if check==0:
        print(f"Sry we currently don't have {product} :(\n")

print("Product Qnty Price")
csv_printer("Bill.csv")
print(f"Sum--------------{bill}")'''


# print("Your Final Bill is",bill,"rs")





data_dict={"Product":[],
       "Price":[],
       "Quantity":[]}

with open("Product.csv") as file:
    csv_file = csv.reader(file)
    next(csv_file)
    for lines in csv_file:
        data_dict["Product"].append(lines[0])
        data_dict["Price"].append(int(lines[1]))
        data_dict["Quantity"].append(lines[2])

for i,j in data_dict.items():
    print(i,j)
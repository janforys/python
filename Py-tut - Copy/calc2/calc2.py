n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
operator = input("Enter an operator you want to calculate: ")

if operator == "+":
    print(n1+n2)
elif operator == "-":
    print(n1-n2)
elif operator == "*":
    print(n1*n2)
elif operator == "/":
    print(n1/n2)
else:
    print("INVALID OPERATOR YOU FOOL ! ! !")


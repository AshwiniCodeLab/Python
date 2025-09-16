Total= input("Enter the total amount: ")
amount = int(Total)
if amount>1000:
	discount = float(amount * 0.1)
	print("Discount is", discount)
	print("Total amount after discount is", amount - discount)


if amount<1000:
    discount = float(amount * 0.05)
    print("Discount is", discount)
    print("Total amount after discount is", amount - discount  )

if amount==1000:
    discount = float(amount * 0.07)
    print("Discount is", discount)
    print("Total amount after discount is", amount - discount  )
    
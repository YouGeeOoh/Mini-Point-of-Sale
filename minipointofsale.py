products = {
    "name" : [],
    "price" : [],
    "quantity":[]
}

def prompt():
    print ("1-> To add product")
    print ("2-> To sell product")
    print ("3-> To view product")
    print ("4-> To delete product")
    print ("5-> To check Account balance")
    print ("6-> Exit")
    userInput = int(input("**Choose your input**\n"))  
    return userInput 

# def addmore():
#     print("1-> To add more products")
#     print("2-> To Exit more products")

running = True
account = 0
while running:
    userInput = prompt()

    if userInput == 1:
        print("* Add your product *")
        try:
            product = input("Enter Product name:\n  ").lower()
            if(product in products['name']):
                print(f"{product}, alredy in stock")
            else:
                products["name"].append(product)
                price = int(input("Input Price: \n"))
                quantity = int(input("Input Quantity:\n"))
                products["price"].append(price)  
                products["quantity"].append(quantity)

                print(f"** {product} Successfully Added!**\n")
        except:
            print("Please give a correct input\n")
            
    elif userInput ==2:
        sell = input("** Enter product to sell:** \n")
        if sell.lower() in products["name"]:
            index = products["name"].index(sell)
            quantity = int(input("** How many would you sell: ** \n"))
            if quantity <= products["quantity"][index]:
                products["quantity"][index] -= quantity
                price = int(input("** Input price ** \n"))
                if price == products["price"][index]:
                    amount = price * quantity
                    account += amount
                    print("f You have sucessfully sold {quantity} {sell} at {amount}")
                    print("income = ", amount)

                elif price <= products["price"][index]:
                    print ("** This price is not upto the bargain**\n")
                elif price >= products["price"][index]:
                    print("** You wanna give us extra for the product?**\n")
            elif quantity > products["quantity"][index]:
                print(f"Sorry, we don't have upto {quantity}")
        else:
            print(f"{sell} not available")

    elif userInput == 3:
        print("Product\t Price\t Quantity")
        for i, name in enumerate(products["name"]):
            priicece = products['price'][i]
            quantity = products["quantity"][i]
            print(f"{name}\t {price}\t {quantity}")
            
    elif userInput == 4:
        deleteproduct = input("** Enter product to delete**")
        if deleteproduct.lower() in products["name"]:
            index = products["name"].index(deleteproduct)
            del products["name"][index]
            del products["price"][index]
            del products["quantity"][index]
            print(f"{deleteproduct} sucessfully deleted")
        else:
            print(f"{deleteproduct} not in stock")

    elif userInput == 5:
        print(f"Your Account Balance is : {account}")

    elif userInput == 6:
        running = False
        print("Exitted!")
    else:
        print("Wrong Input")
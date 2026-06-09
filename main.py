cart = []
prices = {
    "apple": 2,
    "milk": 3,
    "bread": 2
}

total = 0

while True:
    print("SHOPPING CART")
    print("Apple, Milk, Bread")
    print("5 - Checkout")

    item = input("Add item: ").lower()

    if item in prices:
        cart.append(item)
        total += prices[item]
        print(item, "added!")

    elif item == "5":
        print("Items:", cart)
        print("Total: $", total)
        break

    else:
        print("Invalid item!")

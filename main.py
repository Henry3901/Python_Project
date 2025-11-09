def deposit():
    while True:
        amount = input("What amount would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a numeric value.")
    
    return amount

deposit()
# Let user input the amount of money to be changed
def amount():
    amount = int(input("How much money would you like to convert? "))
    while True:
        if amount < 0:
            print("This is not a valid amount. Please try again")
            continue
        break
    return amount

# Let user decide whether or not they want to see supported currencies
def supported_currencies():
    view_currencies = input("Would you like to view supported currencies? Type 'Y' or 'N'. ")
    currencies = ("EUR", "USD", "RUB")
    while True:
        if view_currencies == "Y":
            print(currencies)  
            break
        elif view_currencies == "N":
            break 
        else:
            print("Invalid input. Please try again")
    return

# Let user choose the source currency
def currency_source():
    while True:
        source_choice = input("Choose source currency. ")
        if source_choice in ("EUR", "USD", "RUB"):
            break
        print("Invalid choice. Please select 'EUR', 'USD' or 'RUB'")
    return source_choice

# Let user choose the target currency
def currency_target(source_choice):
    while True:
        target_choice = input("Choose target currency. ")
        if target_choice in ("EUR", "USD", "RUB") and target_choice != source_choice:
            break
        print("Invalid choice. Please select 'EUR', 'USD' or 'RUB' and a differnt currency than the source.")
    return target_choice

# Define the default exchange rates
def exchange_rate(source, target):
        rates = {
        ("USD", "EUR"): 0.85,
        ("EUR", "USD"): 1.1765,
        ("USD", "RUB"): 76,
        ("RUB", "USD"): 0.01316,
        ("EUR", "RUB"): 89.41,
        ("RUB", "EUR"): 0.01118
    }
        return rates

# Ask the user whether they want to change the current exchange rate from the selected source to target
def change_exchange_rate(rates, source, target):
    current_rate = rates[(source, target)]
    while True:
        change_Y_or_N = input(f"This is the current exchange rates: {current_rate}. Would you like to change it? Answer Y or N. ")
        if change_Y_or_N == "Y":
            while True:
                new_rate = float(input(f"You want to change the excange rate from {source} to {target}. The old rate was {current_rate}. What shall be the new exchange rate? "))
                if new_rate <= 0:
                    print("Invalid input. The new exchange rate must be bigger than 0. Please try again")
                else:
                    break
            rates[(source, target)] = new_rate
            return new_rate
        elif change_Y_or_N == "N":
            return current_rate
        else:
            print("Invalid input. Try again")

# function calls
if __name__ == "__main__":
    amount = int(amount())
    supported_currencies()
    source = currency_source()
    target = currency_target(source)
    rates = exchange_rate(source, target)
    current_rate = rates[(source, target)]
    exchangeRate = change_exchange_rate(rates, source, target)
    print(f"Your exchanged amount is {exchangeRate * amount} {target}")
# Let user input the amount of money to be changed
def get_amount():
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

# Let the user have the option to add currencies and thus add exchange rates
def add_currencies(rates):
    while True:
    # User wants to add a new currency? Yes or No
        add_YorN = input("Would you like to add a currency? Type 'Y' or 'N'. ").upper()
        if add_YorN == "Y":
            existing_currencies = set()
            for pair in rates:
                existing_currencies.update(pair)
            while True:
                    new_currency = input("Which currency would you like to add? The input must be a capitalized three letter abreviation. ")
                    if len(new_currency) == 3 and new_currency.isalpha() and new_currency not in existing_currencies:
                        break
                    print("Invalid format or currency already exists. Please try again.")
           
    # Define new exchange rates
            for currency in existing_currencies:
                while True:
                    try:
                        rate = float(input(f"What is the exchange rate from {currency} to {new_currency}? "))
                        if rate <= 0:
                            raise ValueError
                        rates[new_currency, currency] = rate
                        rates[currency, new_currency] = 1 / rate
                        break
                    except ValueError:
                        print("Invalid input. Enter a positive number")
        elif add_YorN == "N":
            break
        else:
            print("Invalid input. Try again.")
# Let user choose the source currency
def currency_source(rates) -> str:
    supported = sorted({c for pair in rates for c in pair})
    while True:
        source_choice = input("Choose source currency. ").upper()
        if source_choice in supported:
            break
        print(f"Invalid choice. Please select in  {', '.join(supported)}: ")
    return source_choice

# Let user choose the target currency
def currency_target(source_choice, rates) -> str:
    supported = sorted({c for pair in rates for c in pair})
    while True:
        target_choice = input("Choose target currency. ").upper()
        if target_choice in supported and target_choice != source_choice:
            break
        print(f"Invalid choice. Please select in {', '.join(supported)}. The target currency has to be different than the source currency.")
    return target_choice

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
    rates: dict = {
    ("USD", "EUR"): 0.85,
    ("EUR", "USD"): 1.1765,
    ("USD", "RUB"): 76,
    ("RUB", "USD"): 0.01316,
    ("EUR", "RUB"): 89.41,
    ("RUB", "EUR"): 0.01118
}
    amount: int = get_amount()
    supported_currencies()
    add_currencies(rates)
    source: str = currency_source(rates)
    target: str = currency_target(source, rates)
    current_rate: float = rates[(source, target)]
    exchangeRate: float = change_exchange_rate(rates, source, target)
    print(f"Your exchanged amount is {round(exchangeRate * amount,1)} {target}")
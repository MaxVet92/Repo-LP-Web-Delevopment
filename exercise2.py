
def get_amount():
    # Let user input the amount of money to be changed
    while True:
        try:
            amount = int(input("How much money would you like to convert? "))
        except ValueError:
            print("This is not a valid amount. Please try again")
        if amount < 0:
            print("This is not a valid amount. Please try again")
        else:
            return amount


def print_supported_currencies():
    # Let user decide whether or not they want to see supported currencies
    currencies = ("EUR", "USD", "RUB")
    while True:
        is_viewing_currencies = input("Would you like to view supported currencies? Type 'Y' or 'N'. ").strip().upper()
        if is_viewing_currencies == "Y":
            print(currencies)  
            return
        elif is_viewing_currencies == "N":
            return 
        else:
            print("Invalid input. Please try again")


def add_currencies(rates) -> dict[tuple, float]:
    # Let the user have the option to add currencies and thus add exchange rates
    while True:
    # User wants to add a new currency? Yes or No
        is_adding_currency = input("Would you like to add a currency? Type 'Y' or 'N'. ").upper()
        if is_adding_currency == "Y":
            existing_currencies = set()
            for pair in rates:
                existing_currencies.update(pair)
            while True:
                    new_currency = input("Which currency would you like to add? The input must be a capitalized three letter abreviation. ").upper()
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
        elif is_adding_currency == "N":
            break
        else:
            print("Invalid input. Try again.")
    return rates

def currency_source(rates) -> str:
    # Let user choose the source currency
    supported = sorted({c for pair in rates for c in pair})
    while True:
        source_choice = input("Choose source currency. ").upper()
        if source_choice in supported:
            break
        print(f"Invalid choice. Please select in  {', '.join(supported)}: ")
    return source_choice


def currency_target(source_choice, rates) -> str:
    # Let user choose the target currency
    supported = sorted({c for pair in rates for c in pair})
    while True:
        target_choice = input("Choose target currency. ").upper()
        if target_choice in supported and target_choice != source_choice:
            break
        print(f"Invalid choice. Please select in {', '.join(supported)}. The target currency has to be different than the source currency.")
    return target_choice


def change_exchange_rate(rates, source, target):
    # Ask the user whether they want to change the current exchange rate from the selected source to target
    current_rate = rates[(source, target)]
    while True:
        change_Y_or_N = input(f"This is the current exchange rates: {current_rate}. Would you like to change it? Answer Y or N. ").upper()
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


def main():
    rates: dict = {
    ("USD", "EUR"): 0.85,
    ("EUR", "USD"): 1.1765,
    ("USD", "RUB"): 76,
    ("RUB", "USD"): 0.01316,
    ("EUR", "RUB"): 89.41,
    ("RUB", "EUR"): 0.01118
}
    amount: int = get_amount()
    print_supported_currencies()
    add_currencies(rates)
    source: str = currency_source(rates)
    target: str = currency_target(source, rates)
    current_rate: float = rates[(source, target)]
    exchangeRate: float = change_exchange_rate(rates, source, target)
    print(f"Your exchanged amount is {round(exchangeRate * amount,1)} {target}")


if __name__ == "__main__":
    main()
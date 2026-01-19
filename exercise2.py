
def amount():
    amount = int(input("How much money would you like to convert?"))
    while True:
        if amount < 0:
            print("This is not a valid amount. Please try again")
            continue
        break
    return amount

def Currency_Source():

    print("What is your source currency?")
    print("EUR, USD, or RUB")
    while True:
        source_choice = input("Choose source currency (1/2/3): ")
        if source_choice in ("EUR", "USD", "RUB"):
            break
        print("Invalid choice. Please select 1, 2, or 3.")
    return source_choice

def Currency_Target(source_choice):

    print("What is your target currency")
    print("EUR, USD, or RUB")
    while True:
        target_choice = input("Choose target currency (1/2/3): ")
        if target_choice in ("EUR", "USD", "RUB") and target_choice != source_choice:
            break
        print("Invalid choice. Please select 1, 2, or 3 and a differnt currency than the source.")
    return target_choice

### Currency
amount = int(amount())
source = Currency_Source()
target = Currency_Target(source)

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

rates = exchange_rate(source, target)
current_rate = rates[(source, target)]

def change_exchange_rate(rates, source, target):
    current_rate = rates[(source, target)]
    while True:
        change_Y_or_N = input(f"This is the current exchange rates: {exchange_rate}. Would you like to change it? Answer Y or N")
        if change_Y_or_N == "Y":
            new_rate = float(input(f"You want to change the excange rate from {source} to {target} from {exchange_rate} to?"))
            rates[(source, target)] = new_rate
            return new_rate
        elif change_Y_or_N == "N":
            return current_rate
        else:
            print("Invalid input. Try again")

exchangeRate = change_exchange_rate(rates, source, target)
print(f"Your exchanged amount is {exchangeRate * amount} {target}")
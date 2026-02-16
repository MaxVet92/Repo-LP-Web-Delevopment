
# Please please please always 2 spaces between the functions

def get_amount():
    # Let user input the amount of money to be changed
    while True:
        try:
            amount = int(input("How much money would you like to convert? "))
            if amount >= 0:
                return amount
        except ValueError:
            pass
        print("This is not a valid amount. Please try again")#


def print_supported_currencies(rates):
    while True:
        is_viewing_currencies = input("Would you like to view supported currencies? Type 'Y' or 'N'. ").strip().upper()
        if is_viewing_currencies == "Y":
            currencies = sorted({c for pair in rates for c in pair})
            print(", ".join(currencies))
            return
        elif is_viewing_currencies == "N":
            return
        else:
            print("Invalid input. Please try again")


def get_existing_currencies(rates: dict[tuple[str, str], float]) -> set[str]:
    # get set of existing currencies from rates dictionary
    existing_currencies: set[str] = set()
    for pair in rates:
        existing_currencies.add(pair[0])
        existing_currencies.add(pair[1])
    return existing_currencies


# I have added | None as currently return type is not str if the user answer N
def get_new_currency(existing_currencies: set) -> str | None:
    while True:
        is_adding_currencies = input("Would you like to add a new currenciy? Type 'Y' or 'N'. ").strip().upper()
        if is_adding_currencies == "Y":
            new_currency = input("Which currency would you like to add? The input must be three letters. ").upper()
            if len(new_currency) == 3 and new_currency.isalpha() and new_currency not in existing_currencies:
                return new_currency
        elif is_adding_currencies == "N":
            return
        else:
            print("Invalid input. Please try again")

        print("Invalid format or currency already exists. Please try again.")


def get_exchange_rate(new_currency: str, existing_currency: str) -> float:
    while True:
        try:
            rate = float(input(f"What is the exchange rate from {new_currency} to {existing_currency}? "))
            if rate <= 0:
                raise ValueError
            return rate
        except ValueError:
            print("Invalid input. Enter a positive number")


# there is a bug in this function if the user answers N, the function will return None, please correct
# as mentioned, more precise type hinting is better, in this case not tuple but tuple[str, str]
def add_currencies(rates: dict[tuple, float]) -> dict[tuple, float]:
    new_rates = rates.copy()
    # Let the user have the option to add currencies and thus add exchange rates
    existing_currencies = get_existing_currencies(new_rates)
    new_currency = get_new_currency(existing_currencies)

    # Define new exchange rates
    for currency in existing_currencies:
        rate = get_exchange_rate(new_currency, currency)
        new_rates[new_currency, currency] = rate
        new_rates[currency, new_currency] = 1 / rate

    return new_rates


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


def change_exchange_rate(rates: dict[tuple[str, str], float], source: str, target: str) -> float:
    """
    Allows user to manually change both source->target and target->source rates.
    Handles invalid float input safely.
    """
    current_rate = rates[(source, target)]
    current_rate_inversed = rates[(target, source)]

    while True:
        change_Y_or_N = input(
            f"Current rates:\n"
            f"{source} -> {target}: {current_rate}\n"
            f"{target} -> {source}: {current_rate_inversed}\n"
            "Would you like to change them? Answer Y or N: "
        ).strip().upper()

        if change_Y_or_N == "Y":
            # get source -> target
            while True:
                try:
                    new_rate_source_to_target = float(input(
                        f"Changing exchange rate from {source} to {target}. Old rate: {current_rate}. New rate: "
                    ))
                    if new_rate_source_to_target <= 0:
                        print("Rate must be greater than 0. Try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                break  # valid input, exit loop

            # get target -> source
            while True:
                try:
                    new_rate_target_to_source = float(input(
                        f"Changing exchange rate from {target} to {source}. Old rate: {current_rate_inversed}. New rate: "
                    ))
                    if new_rate_target_to_source <= 0:
                        print("Rate must be greater than 0. Try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                break  # valid input, exit loop

            # update dictionary
            rates[(source, target)] = new_rate_source_to_target
            rates[(target, source)] = new_rate_target_to_source

            return new_rate_source_to_target  # return the main rate

        elif change_Y_or_N == "N":
            return current_rate
        else:
            print("Invalid input. Please answer Y or N.")


def main():
    rates: dict = {
        ("USD", "EUR"): 0.85,
        ("EUR", "USD"): 1.1765,
        ("USD", "RUB"): 76,
        ("RUB", "USD"): 0.01316,
        ("EUR", "RUB"): 89.41,
        ("RUB", "EUR"): 0.01118
    }

    amount: int = 0  # initialize amount
    exchanged_amount: float | None = None

    while True:
        print("\n=== Currency Exchange Menu ===")
        print("1. Enter amount to exchange")
        print("2. View supported currencies")
        print("3. Add a new currency")
        print("4. Change exchange rate")
        print("5. Exchange money")
        print("6. Exit")

        try:
            choice = int(input("Select an option (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number 1-6.")
            continue

        if choice == 1:
            amount = get_amount()
        elif choice == 2:
            print_supported_currencies(rates)
        elif choice == 3:
            rates = add_currencies(rates)
        elif choice == 4:
            if not rates:
                print("No exchange rates available yet.")
                continue
            source = currency_source(rates)
            target = currency_target(source, rates)
            change_exchange_rate(rates, source, target)
        elif choice == 5:
            if amount <= 0:
                print("Please enter a valid amount first (option 1).")
                continue
            source = currency_source(rates)
            target = currency_target(source, rates)
            current_rate = rates[(source, target)]
            exchange_rate = change_exchange_rate(rates, source, target)
            exchanged_amount = round(exchange_rate * amount, 2)
            print(f"Your exchanged amount is {exchanged_amount} {target}")
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select 1-6.")


if __name__ == "__main__":

    main()
import math

OPENING_BALANCE = 10000.0


def read_amount(prompt):
    """Read a positive, finite amount. Return None if the input is invalid."""
    text = input(prompt).strip()
    try:
        amount = float(text)
    except ValueError:
        print("Error: Please enter a valid number.")
        return None
    if not math.isfinite(amount) or amount <= 0:
        print("Error: Amount must be greater than 0.")
        return None
    return amount


def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def main():
    balance = OPENING_BALANCE
    print("Welcome to Kiran Bank")
    print(f"Opening Balance: ₹{balance:.2f}")

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = read_amount("Enter deposit amount: ")
            if amount is not None:
                balance += amount
                print("Deposit successful.")
                print(f"Updated Balance: ₹{balance:.2f}")

        elif choice == "3":
            amount = read_amount("Enter withdrawal amount: ")
            if amount is not None:
                if amount <= balance:
                    balance -= amount
                    print("Withdrawal successful.")
                    print(f"Updated Balance: ₹{balance:.2f}")
                else:
                    print("Transaction failed: Insufficient balance.")
                    print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
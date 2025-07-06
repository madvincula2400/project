#PRINCIPAL AMOUNT
#INTEREST RATE
#TOTAL INTEREST EARNED

def calculate_compound_interest():
    """Calculate and display compound interest for 5 years"""

    while True:
        try:
            # Get input from user
            principal = float(input("Enter principal amount: "))
            interest_rate = float(input("Enter interest rate: "))

            # Validate input
            if principal <= 0 or interest_rate < 0:
                print("Please enter positive values.")
                continue

            # Initialize variables
            current_balance = principal
            total_interest = 0.0

            # Display header
            print("\nYear    Beginning Balance    Ending Balance")
            print("----    ----------------    --------------")

            # Calculate and display for 5 years
            for year in range(1, 6):
                beginning_balance = current_balance
                annual_interest = current_balance * interest_rate
                ending_balance = current_balance + annual_interest

                # Display year data
                print(f"{year}       ${beginning_balance:>10,.2f}       ${ending_balance:>10,.2f}")

                # Update for next year
                current_balance = ending_balance
                total_interest += annual_interest

            # Display total interest earned
            print(f"\nTotal interest earned: ${total_interest:,.2f}")

            # Ask if user wants to continue
            continue_choice = input("\nCalculate again? (y/n): ").lower()

            if continue_choice != 'y':
                break

        except ValueError:
            print("Please enter numbers only.")
            continue
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

def main():
    """Main function"""
    print("Compound Interest Calculator")
    print("Calculates interest over 5 years")
    print()

    calculate_compound_interest()

if __name__ == "__main__":
    main()








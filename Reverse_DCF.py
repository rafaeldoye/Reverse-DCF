import numpy as np
from scipy.optimize import brentq

def reverse_dcf():
    while True:  # Loop for restarting the analysis
        print("\n--- Reverse DCF Analysis ---\n")

        # Step 1: Input parameters
        try:
            initial_fcf = float(input("Enter the initial Free Cash Flow (FCF) in millions: "))  # FCF in millions
            discount_rate = float(input("Enter the discount rate (as a decimal, e.g., 0.10 for 10%): "))
            years = int(input("Enter the number of years for projection: "))
            terminal_growth_rate = float(input("Enter the terminal growth rate (as a decimal, e.g., 0.03 for 3%): "))
            number_of_shares = float(input("Enter the number of shares outstanding (in millions): "))
            current_price_per_share = float(input("Enter the current price per share (in dollars): "))
        except ValueError:
            print("Invalid input. Please enter numerical values only.")
            continue

        # Step 2: Calculate the market capitalization
        market_cap = current_price_per_share * number_of_shares  # Market capitalization

        # Step 3: Define the DCF function
        def calculate_dcf(growth_rate):
            cash_flows = []
            for year in range(1, years + 1):
                cash_flows.append(initial_fcf * (1 + growth_rate) ** year)
            # Calculate terminal value at the end of projection period
            terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
            cash_flows[-1] += terminal_value  # Add terminal value to the last year's cash flow

            # Discount all cash flows to present value
            discounted_cash_flows = [
                cf / ((1 + discount_rate) ** year) for year, cf in enumerate(cash_flows, start=1)
            ]
            return sum(discounted_cash_flows)

        # Step 4: Find the implied growth rate
        def dcf_difference(growth_rate):
            return calculate_dcf(growth_rate) - market_cap

        try:
            implied_growth_rate = brentq(dcf_difference, -0.5, 1)  # Assumed bounds for growth rate
        except ValueError:
            print("Error: Unable to find a feasible growth rate within the bounds.")
            continue

        print(f"\nImplied growth rate (from reverse DCF): {implied_growth_rate:.6f} (or {implied_growth_rate * 100:.2f}%)")

        while True:  # Loop for adjusting the growth rate
            try:
                desired_growth_rate = float(input("\nEnter your desired growth rate for FCF (as a decimal, e.g., 0.05 for 5%): "))

                # Step 5: Calculate discounted FCFs and terminal value
                future_fcfs = [initial_fcf * ((1 + desired_growth_rate) ** year) for year in range(1, years + 1)]
                discounted_fcfs = [fcf / ((1 + discount_rate) ** (i + 1)) for i, fcf in enumerate(future_fcfs)]
                terminal_value = future_fcfs[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
                discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)

                # Step 6: Calculate total equity value
                total_equity_value = sum(discounted_fcfs) + discounted_terminal_value

                # Step 7: Calculate the intrinsic value per share
                intrinsic_value_per_share = total_equity_value / number_of_shares

                # Step 8: Calculate the upside/downside
                upside_downside = (intrinsic_value_per_share - current_price_per_share) / current_price_per_share * 100

                print(f"\nIntrinsic Value of the company: ${total_equity_value:,.2f} million")
                print(f"Intrinsic Value per share: ${intrinsic_value_per_share:,.2f}")
                print(f"Current price per share: ${current_price_per_share:,.2f}")
                print(f"Upside/Downside: {upside_downside:.2f}%")

                restart_option = input("\nDo you want to try another growth rate? (yes/no): ").strip().lower()
                if restart_option != 'yes':
                    break

            except ValueError:
                print("Invalid input. Please enter a numerical value for the growth rate.")

        restart_analysis = input("\nDo you want to restart the analysis from the beginning? (yes/no): ").strip().lower()
        if restart_analysis != 'yes':
            print("\nThank you for using the Reverse DCF Analysis tool. Goodbye!")
            break

if __name__ == "__main__":
    reverse_dcf()

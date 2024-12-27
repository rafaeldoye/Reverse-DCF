import numpy as np

def reverse_dcf():
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
        return

    # Step 2: Define a function to calculate the present value of cash flows
    def present_value(cash_flows, rate):
        return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cash_flows, start=1))

    # Step 3: Reverse engineering to find implied growth rates
    def calculate_fcf_with_growth(initial_fcf, growth_rate, years):
        return [initial_fcf * ((1 + growth_rate) ** year) for year in range(1, years + 1)]

    def find_implied_growth(target_value):
        low, high = 0, 0.5  # Reasonable bounds for growth rate search (0% to 50% growth)
        tolerance = 1e-6
        iteration = 0

        while high - low > tolerance and iteration < 100:
            mid = (low + high) / 2
            future_fcfs = calculate_fcf_with_growth(initial_fcf, mid, years)
            terminal_value = future_fcfs[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
            total_value = present_value(future_fcfs, discount_rate) + terminal_value / ((1 + discount_rate) ** years)

            if total_value < target_value:  # If the total value is lower than the target, adjust bounds
                low = mid
            else:
                high = mid

            iteration += 1

        return (low + high) / 2

    # Step 4: Calculate implied growth rate from DCF
    market_cap = current_price_per_share * number_of_shares  # Market capitalization
    implied_growth_rate = find_implied_growth(market_cap)

    print(f"\nImplied growth rate (from reverse DCF): {implied_growth_rate:.6f} (or {implied_growth_rate * 100:.2f}%)")

    # Step 5: Calculate the intrinsic value of the company
    future_fcfs = calculate_fcf_with_growth(initial_fcf, implied_growth_rate, years)
    terminal_value = future_fcfs[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    intrinsic_value = present_value(future_fcfs, discount_rate) + terminal_value / ((1 + discount_rate) ** years)

    # Step 6: Calculate the intrinsic value per share
    intrinsic_value_per_share = intrinsic_value / number_of_shares

    # Step 7: Calculate the upside/downside
    upside_downside = (intrinsic_value_per_share - current_price_per_share) / current_price_per_share * 100

    print(f"\nIntrinsic Value of the company: ${intrinsic_value:,.2f} million")
    print(f"Intrinsic Value per share: ${intrinsic_value_per_share:,.2f}")
    print(f"Current price per share: ${current_price_per_share:,.2f}")
    print(f"Upside/Downside: {upside_downside:.2f}%")

    # Step 8: Calculate the implied growth rate at current price
    implied_growth_rate_current_price = find_implied_growth(market_cap)
    print(f"\nThe company is currently priced assuming a growth rate of: {implied_growth_rate_current_price * 100:.2f}%")

if __name__ == "__main__":
    reverse_dcf()

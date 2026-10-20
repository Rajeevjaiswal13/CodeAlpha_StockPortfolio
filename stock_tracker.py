# CodeAlpha Internship Task: Stock Portfolio Tracker

import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock symbol. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "Stock": stock,
        "Price": price,
        "Quantity": quantity,
        "Investment": investment
    })

    print(f"Added {quantity} shares of {stock}.")
    print(f"Investment value: ${investment:.2f}")

print("\n" + "=" * 40)
print("         PORTFOLIO SUMMARY")
print("=" * 40)

if portfolio:
    for item in portfolio:
        print(
            f"{item['Stock']}: "
            f"{item['Quantity']} shares × "
            f"${item['Price']} = "
            f"${item['Investment']:.2f}"
        )

    print("-" * 40)
    print(f"Total Investment: ${total_investment:.2f}")

    # Save portfolio to CSV
    with open("portfolio.csv", "w", newline="") as file:
        fieldnames = [
            "Stock", "Price", "Quantity", "Investment"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(portfolio)

    print("Portfolio saved to portfolio.csv")

else:
    print("No stocks were added to your portfolio.")

print("\nThank you for using Stock Portfolio Tracker!") 
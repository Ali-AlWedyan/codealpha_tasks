import yfinance as yf
import pandas as pd
import warnings

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

def add_stock(ticker:str , tickers:dict):
    # Add a stock ticker to the portfolio.
    if ticker not in tickers:

        try:
            temp = yf.Ticker(ticker)
            temp = pd.DataFrame(temp.history(period="1d"))
            price = temp['Close'][-1]
            
            print(f"The price for '{ticker}' is ${price:.2f} per unit")
            amount = int(input("How many do you want to buy: "))
            
            tickers[ticker] = {'price': price, 'amount': amount}
            print(f"You have bought {amount} of '{ticker}', which costed {price * amount:.2f}")

        except Exception:
            print(f"Ticker '{ticker}' probably does not exist.")

    else:
        print(f"{ticker} is already in your portfolio.")

    return

def remove_stock(tickers:dict):
    # Remove a stock ticker from the portfolio.
    if not display_performance(tickers):
        return
    ticker = input("Enter the stock ticker to remove: ").strip().upper()

    if ticker in tickers:
        tickers.pop(ticker)
        print(f"{ticker} has been removed from your portfolio.")

    else:
        print(f"{ticker} is not in your portfolio.")

    return

def display_performance(tickers:dict):
    if len(tickers) == 0:
        print("Your portfolio is empty.")
        return  False
    
    # data = yf.download(tickers, period="1d", group_by='ticker')
    print("Stock\tPrice\tAmount\tTotal")
    for ticker, info in tickers.items():
        price, amount = info["price"], info["amount"]
        print(f"{ticker}\t${price:.2f}\t{amount}\t{price*amount:.2f}")
    return True

def main():
    # Initialize an empty dict to hold stock tickers
    tickers = dict()
    print("Welcome to your portofolio!")

    while True:
        print("""
Enter one of the following
1) 'add' to add a stock
2) 'remove' to remove a stock
3) 'track' to track performance
4) 'exit' to exit the program""")
        action = input("\nEnter Command or Number: ").strip().lower()
        print()
        if action == "add" or action =="1":    
            ticker = input("Enter the stock ticker to add: ").strip().upper()
            add_stock(ticker, tickers)

        elif action == 'remove' or action =='2':
            remove_stock(tickers)

        elif action == 'track' or action =='3':
            display_performance(tickers)

        elif action == 'exit' or action =='4':
            print("Exiting the portfolio tracker.")
            break

        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()

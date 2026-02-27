import csv
from datetime import datetime

def save_to_csv(d):
    today_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"market_report_{today_date}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Currency Symbol', 'Current Price (USD)'])

        for t in d:
            writer.writerow([t.symbol, t.price])
            
    print(f"Success: Market data securely saved to {filename}")
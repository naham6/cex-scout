from dataclasses import dataclass

@dataclass
class curr:
    symbol: str
    price: float

    def display_info(self):
        #printing the data.
        print(f"Currency: {self.symbol} and Current Price: ${self.price:.4f}")